from MIT_Stage_Uniformity_plotting import *

def Single_stage_uniformity_velocity_graph():
    ''' Graphs a single stage uniformity data set. '''
    
    df = get_stage_uniformity_df()
    df = add_best_fit_line(df,'Time','Z')
    
    plot_diff_column_values(df,['X','Z'])

    plt.ylabel('difference between two values')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()


def Single_stage_uniformity_best_fit_graph():
    ''' Graphs a single stage uniformity data set. '''
    
    df = get_stage_uniformity_df()
    df = add_best_fit_line(df,'Time','Z')
    
    edge = 1

    
    plt.scatter(df['Time'][edge:-edge],df['Z'][edge:-edge], s= 1, label = 'actual')
    plt.plot(df['Time'][edge:-edge],df['best_fit_time'][edge:-edge], label = 'Best fit', color = 'red')

    plt.ylabel('difference between two values')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()

    