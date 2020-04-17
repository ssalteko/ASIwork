import pandas as pd
import matplotlib.pyplot as plt

from regression import *

def get_dfn_dfp(df):
    ''' returns two dfs for a two step file, one with a positive slope, and one negative'''
    l = len(df)
    # print("l: ",l)


def scan_test_frame(file):
    '''Returns a pandas Data Frame from a stability test data file.'''
    #### TODO = make the header detect the data in case the header size changes in the future.
    scan_test_frame = pd.read_csv(file, sep=',', header=1)
    scan_test_frame['Axis(mm)'] = scan_test_frame['Axis']/10000
    scan_test_frame['Axis(mm)abs'] = scan_test_frame['Axis(mm)'] - scan_test_frame['Axis(mm)'][0]
    scan_test_frame['Z(um)'] = scan_test_frame['Z']/10
    scan_test_frame['Z(um)abs'] = scan_test_frame['Z(um)'] - scan_test_frame['Z(um)'][0]
    scan_test_frame['Time_abs'] = scan_test_frame['Time'] - scan_test_frame['Time'][0]


    return scan_test_frame

def add_regression_lines(df,df_info_dict):
    ''' adds regression lines to a given df.'''
    
    ss_tt = get_ss_xx(df,'Time_abs')
    ss_tz = get_ss_xy(df,'Time_abs','Z(um)abs')
    b1_time = get_b1(ss_tt,ss_tz)
    
    if df_info_dict.get('actual_speed'):
        df_info_dict['actual_speed'] = b1_time
    else:
        print('type ',type(int(df['Move'][1])))
        move = str(df['Move'][1])
        name = 'actual_speed_' + move
        df_info_dict[name] = b1_time

    b0_time = get_b0(df['Time_abs'],df['Z(um)abs'],b1_time)
    b1_theoretical = -df_info_dict['speed']*10**-6

    # print("b1_time",b1_time)
    # print("b0_time",b0_time)
    # print(df.head())
    # print("b1_theoretical: ", b1_theoretical)

    i = 0
    while i < len(df):
        t = b1_time*df['Time_abs'][i]
        v = b1_theoretical*df['Time_abs'][i]
        df.loc[i,'Time_slope'] = b0_time + t
        # print(df['Time_slope'][0])
        # print("b0_time: ",b0_time)
        df.loc[i,'th_slope'] = b0_time + 7 + v ##b0_time because if the other time_slope graph stated at the same place it should have
                                           ## a slope that is equal.
        i += 1
    
    df['regLine_z_diff'] = df['Time_slope'] - df['Z(um)abs']
    
    # scan_test_frame['Z(um)abs_time_slope_corected'] = scan_test_frame['Z(um)abs'] - scan_test_frame['time_slope']

    return df,df_info_dict

def reset_time(df):
    '''Creates a time_abs column in a given dataframe'''
    df['Time_abs'] = df['Time_abs']-df['Time_abs'][0]
    return df

def get_df_list(data_list, directory):
    ''' takes a list of data files and a directory and returns a list of dataframes'''
    df_list = []

    for data in data_list:
        df = {}
        data_name = data[0:-4]
        df[data_name] = hekka_z_test_frame(directory + "/" + data)
        df_list += [df[data_name]]
    return df_list


def graph_all_scatter(df_list,dependant,independant,fig,axs):
    ''' Graphs a list of data frames as scatter plots. '''

    for df in df_list:
        axs.scatter(df[dependant],df[independant])
    
    
