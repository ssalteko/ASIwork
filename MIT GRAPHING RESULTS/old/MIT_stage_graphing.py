from matplotlib import pyplot as plt
from file_manager import *
from MIT_stage_uniformity import *

def graph_single_uniformity_test():
    ''' Graphs a directory of scan motion files. '''

    file_name = get_file_name()
    # file_name =  'C:/Users/ASI_Test/Desktop/MIT Stage/ztest_2020-03-16_13-16-40_distance-10000.txt'
    # file_name = 'C:/Users/ASI_Test/Desktop/MIT Stage/ztest_2020-03-16_13-07-56_distance-10000.txt'
    # file_name = "C:/Users/Steve/Desktop/MIT_Stage_uniformity/MIT Stage/MIT Stage/ztest_2020-03-16_13-07-56_distance-10000.txt"
    # file_name = 'C:/Users/ASI_Test/Desktop/MIT Stage/ztest_2020-03-16_13-17-23_distance-10000.txt'
    file_info_dict = get_file_info_dict(file_name)
    
    df = scan_test_frame(file_name)
    l = len(df)
    half = l//2
    ep = round(0.2*half)

    dfn = df.iloc[ep:half-ep].reset_index()
    #dfp = dfn.iloc[half:l].reset_index()
    dfp = df[half + ep: -ep].reset_index()
    dfn,file_info_dict = add_regression_lines(dfn,file_info_dict)
    dfp,file_info_dict = add_regression_lines(dfp,file_info_dict)
    
    dfp = reset_time(dfp)
    dfn = reset_time(dfn)

    print(file_info_dict)
    print('dfp.head:\n ', dfp.head())
    print('dfp.head:\n ', dfn.head())

    print('dfp.tail:\n ', dfp.tail())
    print('dfn.tail:\n ', dfn.tail())

    # print("file_name: ",file_name)
    # print(file_info_dict)
    # print(half)
    # print("ep: ",ep)
    # print("dfp.head",dfp.head())


    # print("dfn head:\n",dfn.head())
    # print("dfn tail:\n",dfn.tail())

    # print(dfn.head())
    
    speed = file_info_dict['speed']
    plt.figure(num =  3)
    ax = plt.axes()

    ax.set_facecolor("black")
    plt.scatter(x=dfn['Time_abs'], y = dfn['Z(um)abs'])
    plt.grid(color = 'white')
    plt.scatter(x=dfp['Time_abs'], y = dfp['Z(um)abs'])
    plt.plot(dfn['Time_abs'],dfn['Time_slope'], c = 'red')
    plt.plot(dfn['Time_abs'],dfn['th_slope'], c = 'yellow')
    plt.plot(dfp['Time_abs'],dfp['Time_slope'], c = 'green')
    plt.plot(dfp['Time_abs'],dfp['th_slope'], c = 'Orange')
    
    plt.title(f'speed: {speed}')
    
    plt.figure(num = 2)
    
    plt.scatter(dfn['Time_abs'],dfn['regLine_z_diff'], c = 'green')

    
    plt.style.use('dark_background')
    print((dfn['regLine_z_diff'].std()))
    print((dfp['regLine_z_diff'].std()))
    plt.show()