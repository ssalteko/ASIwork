import matplotlib.pyplot as plt

from MIT_Stage_Uniformity_pandas import *

def plot_diff_column_values(df,columns):
    ''' plots a given column of a given dataframe. '''
    df = add_diff_columns(df,columns) 
    # print(df)
    ax1 = df.iloc[20:-20].plot( x = 'Time', y = f'{columns[0]}diff', kind = 'scatter', color = 'red', label = f'{columns[0]}diff')
    
    if len(columns) > 1:
        for column in columns[1]:
            df.iloc[20:-20].plot(x = 'Time', y = f'{column}diff', kind = 'scatter', label = f'{column}diff', ax = ax1)
    # plt.plot

