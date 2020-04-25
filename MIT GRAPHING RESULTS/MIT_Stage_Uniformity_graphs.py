from MIT_Stage_Uniformity_plotting import *


def Single_stage_uniformity_velocity_graph(file):
    ''' Graphs a single stage uniformity data set. '''
    
    df = get_stage_uniformity_df(file)
    df = add_best_fit_line(df,'Time','Z')
    
    fig = plt.figure(num = 'Uniformity data')
    plot_diff_column_values(df,['X','Z'])

    plt.ylabel('um')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()



def Single_stage_uniformity_best_fit_graph(file):
    ''' Graphs a single stage uniformity data set. '''
    
 

    df = get_stage_uniformity_df(file)
    # df = df[edge:-edge]  #This cuts the ends off of the data to look at plateaued motion.
    df = df.reset_index() #Reset the index to help the next function not freaK!
    
    fig = plt.figure(num = 'Best fit and Data')
    plot_best_fit_line(df)
  
    plt.ylabel('um')
    plt.xlabel('time (ms)')
    plt.suptitle('Line of best fit with data')
    plt.legend()



def Single_stage_deviation(file):
    ''' Graphs datas deviation from it's best fit line.'''


    df = get_stage_uniformity_df(file)
    # df = df[edge:-edge]  #This cuts the ends off of the data to look at plateaued motion.
    df = df.reset_index() #Reset the index to help the next function not freaK!
 
    fig = plt.figure(num = 'Deviations from best fit')
    plot_best_fit_deviations(df)
  
    plt.xlabel('time (ms)')
    plt.ylabel('um')
    plt.suptitle('Difference between data and \n line of best fit')
    plt.legend()



def group_RMS_by_speed(directory):
    ''' Graphs the deviations from a directory of files.'''
    

    data_list = get_data_list(directory)  ##Get the list of files to be parsed
    
    df_info_dict = get_df_info_dict(directory)  ##Get the dictionary of the headers keyed to their file name.
    df_dict = get_df_dict(directory)  ## Get the dictionary of the dfs keyed to their file name.
    
    df = get_speed_rms_df(df_dict, df_info_dict)

    fig = plt.figure(num = 'rms vs speed', figsize = (12,7))
    plot_rms_by_speed(df)

    plt.xlabel('speed (mm/s)')
    plt.ylabel('um')
    # plt.xscale('log')
    plt.suptitle('4TPI Scan MS 8000 \nRMS vs Speed')
