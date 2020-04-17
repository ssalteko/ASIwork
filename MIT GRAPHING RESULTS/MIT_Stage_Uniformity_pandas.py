import pandas as pd
from file_manager import *
import matplotlib.pyplot as plt


def get_stage_uniformity_df():
    '''get the df for the stage speed uniformity test.'''

    file = get_file_name()
    df = pd.read_csv(file, header = 1)
    df['Z'] = -df['Z']
    # add_diff_columns(df,['X','Z'])

    return df

def add_diff_columns(df,columns):

    for column in columns:
        df[f'{column}diff'] = df[f'{column}'].diff()

    return df
    