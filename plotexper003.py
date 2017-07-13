import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111)
##ax = fig.gca(projection='3d')
x=(-5,-2,-1,0,1)
y=(1,2,3,4,5)
#z=(3,2),(4,5),(6,7)
ax.scatter(x,y)
fig.show()



###Yes negatives are great.
