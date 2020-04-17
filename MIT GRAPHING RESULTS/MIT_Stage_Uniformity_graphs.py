from MIT_Stage_Uniformity_plotting import *

def Single_stage_uniformity_graph():
    ''' Graphs a single stage uniformity data set. '''

    df = get_stage_uniformity_df()

    fig = plt.figure(num = 'Single Stage Uniformity Graph')
    plt.subplot(111)
    plt.suptitle('Difference between successive moves')

    plot_diff_column_values(df,['X','Z'])
    plt.ylabel('difference between two values')

    plt.legend()
    