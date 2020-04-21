from numpy import mean

def get_ss_xx(df,x):
    ''' calculates and returns ss_xx'''
    # print('gh: lenx ',len(df[x]))
    x_squared_sum = 0
    sum_x = sum(df[x])
    for t in df[x]:
        x_squared_sum += t**2
    ss_xx = x_squared_sum - ((sum(df[x])**2)/len(df[x])) 
    return ss_xx

def get_ss_xy(df,x,y):
    '''calculates and returns ss_xy'''
    x_y_sum = 0
    
    i = 0
    l = len(df[x])

    while i < l:
        # print(f"x[{i}]*[y{i}] = {df[x][i]*df[y][i]}")
        # print(i)
        x_y_sum += df[x][i]*df[y][i]
        i += 1

    ss_xy = x_y_sum - (sum(df[x])*sum(df[y])/len(df[x]))
    return ss_xy

def get_b1_0(ss_xx,ss_xy):
    '''calculates and retruns b1'''
    b1 = ss_xy/ss_xx
    return b1

def get_b0(x,y,b1):
    ''' calculates and return b0'''
    b0 = mean(y)-b1*mean(x)
    return b0


def get_b1(df,x,y):
    '''calculates and retruns b1'''
    
    b1_time =  get_ss_xy(df,x,y)/get_ss_xx(df,x)

    return b1_time

# get_ss_xx(df,x)
# x = [25,28,28,27,23]
# y = [34,41,45,38,25]

# x = [2.4,1.6,2.0,2.6,1.4,1.6,2.0,2.2]
# y = [225,184,220,240,180,184,186,215]

# ss_xx = get_ss_xx(x)
# ss_xy = get_ss_xy(x,y)
# b1 = get_b1(ss_xx,ss_xy)
# b0 = get_b0(x,y,b1)
# print('ss_xx',ss_xx) #should be 18.8
# print('ss_xy',ss_xy) #should be 64.4
# print('b1', b1) #should be 3.4255
# print('b0',b0)
