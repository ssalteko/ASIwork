from MIT_Stage_Uniformity_plotting import *

def Single_stage_uniformity_velocity_graph(file):
    ''' Graphs a single stage uniformity data set. '''
    
    df = get_stage_uniformity_df(file)
    df = add_best_fit_line(df,'Time','Z')
    
    plot_diff_column_values(df,['X','Z'])

    plt.ylabel('um')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()



def Single_stage_uniformity_best_fit_graph(file):
    ''' Graphs a single stage uniformity data set. '''
    
    edge = 15

    df = get_stage_uniformity_df(file)
    df = df[edge:-edge]  #This cuts the ends off of the data to look at plateaued motion.
    df = df.reset_index() #Reset the index to help the next function not freaK!
 
    plot_best_fit_line(df)
  
    plt.ylabel('um')
    plt.xlabel('time (ms)')
    plt.suptitle('Line of best fit with data')
    plt.legend()



def Single_stage_deviation(file):
    ''' Graphs datas deviation from it's best fit line.'''

    edge = 15

    df = get_stage_uniformity_df(file)
    df = df[edge:-edge]  #This cuts the ends off of the data to look at plateaued motion.
    df = df.reset_index() #Reset the index to help the next function not freaK!
 
    plot_best_fit_deviations(df)
  
    plt.xlabel('time (ms)')
    plt.ylabel('um')
    plt.suptitle('Difference between data and \n line of best fit')
    plt.legend()



def group_stage_deviation():
    ''' Graphs the deviations from a directory of files.'''
    directory = 'C:/GitSteve/ASIwork/MIT GRAPHING RESULTS/sample_data/MS_8000 20_4_2020'
    
    edge = 15

    data_list = get_data_list(directory)  ##Get the list of files to be parsed

    df_info_dict = get_df_info_dict(directory)  ##Get the dictionary of the headers keyed to their file name.
    df_dict = get_df_dict(directory, edge)  ## Get the dictionary of the dfs keyed to their file name.
    
    df = pd.DataFrame()  ##Empty df to concat to.

    for data in data_list:
        
        # print('speed: ',df_info_dict[data]['speed'])
        speed = df_info_dict[data]['speed']
        # print('rms: ',get_column_RMS(df_dict[data],'best_fit_diff'))
        rms = get_column_RMS(df_dict[data],'best_fit_diff')
        treatment = pd.DataFrame({data:[rms,speed]})
        df = pd.concat([df,treatment], axis = 1)

#### NOT DONE!!!!!!!!!
        
    # print(df)

def group_RMS_by_speed():
    ''' Graphs the deviations from a directory of files.'''
    directory = 'C:/GitSteve/ASIwork/MIT GRAPHING RESULTS/sample_data/MS_8000 20_4_2020'
    
    edge = 15

    data_list = get_data_list(directory)  ##Get the list of files to be parsed

    df_info_dict = get_df_info_dict(directory)  ##Get the dictionary of the headers keyed to their file name.
    df_dict = get_df_dict(directory, edge)  ## Get the dictionary of the dfs keyed to their file name.
    
    df = pd.DataFrame()  ##Empty df to concat to.

    for data in data_list:
        
        # print('speed: ',df_info_dict[data]['speed'])
        speed = df_info_dict[data]['speed']
        # print('rms: ',get_column_RMS(df_dict[data],'best_fit_diff'))
        rms = get_column_RMS(df_dict[data],'best_fit_diff')
        treatment = pd.DataFrame({data:[rms,speed]})
        df = pd.concat([df,treatment], axis = 1)
    df = df.rename(index={0: "speed", 1: "rms"})
    print(df.T.sort_values(by=['speed']))


