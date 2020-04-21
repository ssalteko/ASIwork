import pandas as pd
from file_manager import *
import matplotlib.pyplot as plt
from regression import*


def get_stage_uniformity_df():
    '''get the df for the stage speed uniformity test.'''
    
    file = get_file_name()
    df = pd.read_csv(file, header = 1)

    # print(df)

    df['Z'] = -df['Z']
    df['Xabs'] = df['X'] - df['X'][0]
    df['Zabs'] = df['Z'] - df['Z'][0]

    # print(df)


    return df

def add_diff_columns(df,columns):

    for column in columns:
        df[f'{column}diff'] = df[f'{column}'].diff()

    return df

def add_best_fit_line(df,x,y):
    '''takes data and returns best fit line.'''
    b1_time = get_b1(df,x,y)
    b0_time = get_b0(df[x],df[y],b1_time)
    # print(b0_time,'\n\n\n')
    # [print(b1_time,'\n\n\n')]

    df['best_fit_time'] = df['Time']*b1_time + b0_time
    print(df[0:50])

    return df

def add_best_fit_diff(df):
    ''' Finds the difference between the best fit diff and what it was calculated from.'''
    df['best_fit_diff'] = abs(df['best_fit_time'] - df['Z'])
    return df
