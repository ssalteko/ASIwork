import matplotlib.pyplot as plt
from MIT_Stage_Uniformity_pandas import *


def plot_diff_column_values(df,columns):
    ''' plots a given column of a given dataframe. '''

    df = add_diff_columns(df,columns) 

    ax1 = plt.scatter( x = df['Time'], y = df[f'{columns[0]}diff'], color = 'red', label = f'{columns[0]}diff')
    
    if len(columns) > 1:

        for column in columns[1]:

            plt.scatter(x = df['Time'], y = df[f'{column}diff'], label = f'{column}diff')



def plot_best_fit_line(df):
    ''' Plots a best fit line. '''
    
    df = add_best_fit_line(df,'Time','Z') #This adds a best fit line from the truncated dataframe.
    df = add_best_fit_diff_column(df) #This adds the column that is the diff between Z and the best fit line.
   
    plt.scatter(df['Time'],df['Z'], s= 5, label = 'actual')
    plt.plot(df['Time'],df['best_fit_time'], label = 'Best fit', color = 'red')



def plot_best_fit_deviations(df):
    ''' Plots the difference between the best fit line and it's data.'''

    df = add_best_fit_line(df,'Time','Z') #This adds a best fit line from the truncated dataframe.
    df = add_best_fit_diff_column(df) #This adds the column that is the diff between Z and the best fit line.
   
    plt.plot(df['Time'],df['best_fit_diff'])



def plot_rms_by_speed(df):
    ''' plot the rms by speed for a parsed df.'''
    print(df)
    plt.plot(df['speed'],df['rms'], marker = 'o')
    for a,b in zip(df['speed'], df['rms']): 
        plt.text(a, b, str(round(b,2)))