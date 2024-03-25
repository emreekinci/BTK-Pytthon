import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2 #2


# fig, axs = plt.subplots(2,2)

# 1
# figure = plt.figure()

# axes_cube = figure.add_axes([0.1,0.1,0.85,0.85]) # left,bottom,width,height in percentage of the figure width/height
# axes_cube.plot(x,y, 'b')
# axes_cube.set_xlabel("X axis")
# axes_cube.set_ylabel("Y axis")
# axes_cube.set_title("cube")

# axes_square = figure.add_axes([0.2,0.6,0.25,0.3]) 
# axes_square.plot(x,z, 'r')
# axes_square.set_xlabel("X axis")
# axes_square.set_ylabel("Y axis")
# axes_square.set_title("square")
# plt.legend()

# 2
# figure = plt.figure()

# axes = figure.add_axes([0,0,1,1])
# axes.plot(x,z,label = "Square")
# axes.plot(x,y,label = "Cube")
# axes.legend(loc=1) # 1,2,3,4,--> right-top, left-top....
# plt.show()

# 3
fig, axes = plt.subplots(nrows=2,ncols=1, figsize= (8,8)) # figure  size -->  (8,8)
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.png") # save figure  to file
plt.show()
