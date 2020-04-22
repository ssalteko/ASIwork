import pandas as pd
from file_manager import *
import matplotlib.pyplot as plt
from regression import*


def get_stage_uniformity_df(file):
    '''get the df for the stage speed uniformity test.'''
    
    df = pd.read_csv(file, header = 1)

    df['Z'] = df['Z']/10 #### Convert to microns.

    return df



def add_diff_columns(df,columns):
    ''' adds a difference column here with the diff suffix.'''

    for column in columns:

        df[f'{column}diff'] = df[f'{column}'].diff()

    return df



def add_best_fit_line(df,x,y):
    '''takes data and returns best fit line.'''

    
    b1_time = get_b1(df,x,y)
    b0_time = get_b0(df[x],df[y],b1_time)

    df['slope'] = b1_time

    df['best_fit_time'] = df['Time']*b1_time + b0_time
 
    return df



def add_best_fit_diff_column(df):
    ''' Finds the difference between the best fit diff and what it was calculated from.'''

    df['best_fit_diff'] = df['best_fit_time'] - df['Z']

    return df



def get_df_info_dict(directory):
    ''' gets a dict of dfs from a given directory. '''

    data_list = get_data_list(directory)

    df_info_dict = {}
    
    for data in data_list:

        df_info_dict[data] = get_file_info_dict(f'{directory}/{data}')

    return  df_info_dict



def get_df_dict(directory, edge):
    ''' gets a dict of dfs from a given directory. '''

    data_list = get_data_list(directory)
    
    df_dict = {}

    for data in data_list:

        df_dict[data] = get_stage_uniformity_df(f'{directory}/{data}')[edge:-edge].reset_index()
        df_dict[data] = add_best_fit_line(df_dict[data],'Time','Z')
        df_dict[data] = add_best_fit_diff_column(df_dict[data])

    return df_dict



def  get_column_RMS(df,column):
    ''' get the RMS of a column.'''
    
    rms = ((df[column]**2).sum())/len(df)
    
    return rms



def get_speed_rms_df(df_dict,df_info_dict):
    ''' Returns a df of each treatments speed and rms.'''

    data_list = list(df_dict.keys())

    df = pd.DataFrame()  ##Empty df to concat to.

    for data in data_list:
        
        speed = df_info_dict[data]['speed']
        rms = get_column_RMS(df_dict[data],'best_fit_diff')
        treatment = pd.DataFrame({data:[speed,rms]})
        df = pd.concat([df,treatment], axis = 1)

    df = df.rename(index = {0: "speed", 1: "rms"})
    df = df.T.sort_values(by = ['speed'])
    
    return df
