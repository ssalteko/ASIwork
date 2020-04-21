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
    
    edge = 15

    df = get_stage_uniformity_df()
    df = df[edge:-edge]  #This cuts the ends off of the data to look at plateaued motion.
    df = df.reset_index() #Reset the index to help the next function not freaK!
    print(df)
    
    df = add_best_fit_line(df,'Time','Z') #This adds a best fit line from the truncated dataframe.
    
    print(df)

    
    plt.scatter(df['Time'],df['Z'], s= 5, label = 'actual')
    plt.plot(df['Time'],df['best_fit_time'], label = 'Best fit', color = 'red')

    plt.ylabel('difference between two values')
    plt.xlabel('time (ms)')
    plt.suptitle('Difference between successive moves')
    plt.legend()

    