from MIT_Stage_Uniformity_graphs import *


def main():
    # directory = 'C:/GitSteve/ASIwsork/MIT GRAPHING RESULTS/sample_data/MS_8000 20_4_2020'
    # directory = 'C:/Steve/ASI/asi_github/ASIwork/MIT GRAPHING RESULTS/sample_data/MS_8000 22_4_2020'

    # file = get_file_name()
    directory = get_directory()

    # Single_stage_uniformity_velocity_graph(file)
    # Single_stage_uniformity_best_fit_graph(file)
    # Single_stage_deviation(file)
    group_RMS_by_speed(directory)

    #### group_stage_deviation() #not necessary or working.
    
    
    plt.show()
    
    return
 


if __name__ == '__main__':
    main()