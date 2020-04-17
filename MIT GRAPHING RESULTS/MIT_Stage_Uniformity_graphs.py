from MIT_Stage_Uniformity_plotting import *

def Single_stage_uniformity_velocity_graph():
    ''' Graphs a single stage uniformity data set. '''

    df = get_stage_uniformity_df()
    
    plot_diff_column_values(df,['X','Z'])

    plt.ylabel('difference between two values')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()

    