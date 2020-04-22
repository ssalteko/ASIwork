import matplotlib.pyplot as plt

from MIT_Stage_Uniformity_pandas import *

def plot_diff_column_values(df,columns):
    ''' plots a given column of a given dataframe. '''

    df = add_diff_columns(df,columns) 

    ax1 = df.plot( x = 'Time', y = f'{columns[0]}diff', kind = 'scatter', color = 'red', label = f'{columns[0]}diff')
    
    if len(columns) > 1:
        for column in columns[1]:
            df.plot(x = 'Time', y = f'{column}diff', kind = 'scatter', label = f'{column}diff', ax = ax1)



def plot_best_fit_line(df):
    ''' Plots a best fit line. '''
    
    df = add_best_fit_line(df,'Time','Z') #This adds a best fit line from the truncated dataframe.
    df = add_best_fit_diff_column(df) #This adds the column that is the diff between Z and the best fit line.
   
    ax1 = df.plot('Time','Z', s= 5, kind = 'scatter', label = 'actual')
    df.plot('Time','best_fit_time', label = 'Best fit', color = 'red', ax = ax1)



def plot_best_fit_deviations(df):
    ''' Plots the difference between the best fit line and it's data.'''

    df = add_best_fit_line(df,'Time','Z') #This adds a best fit line from the truncated dataframe.
    df = add_best_fit_diff_column(df) #This adds the column that is the diff between Z and the best fit line.
   
    df.plot('Time','best_fit_diff')

