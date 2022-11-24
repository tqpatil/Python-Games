#Name: Tanishq Patil

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # in this code it is not required


ax = plt.axes(projection='3d')    # create a 3D Cartesian coordinate system
z=[0,50]
y=[0,0]
x=[-10,-10]
ax.plot3D(x,y,z,"green")
a=[0,0]
b=[0,0]
c=[-10,50]
ax.plot3D(c,b,a, "green")
d=[0,50]
e=[0,0]
f=[50,50]
ax.plot3D(f,e,d,"green")
g=[50,50]
h=[0,0]
i=[-10,50]
ax.plot3D(i,h,g,"green")
z=[0,50]
y=[50,50]
x=[-10,-10]
ax.plot3D(x,y,z,"green")
a=[0,0]
b=[50,50]
c=[-10,50]
ax.plot3D(c,b,a, "green")
d=[0,50]
e=[50,50]
f=[50,50]
ax.plot3D(f,e,d,"green")
g=[50,50]
h=[50,50]
i=[-10,50]
ax.plot3D(i,h,g,"green")
x= [-10,-10]
y=[0,50]
z=[0,0]
ax.plot3D(x,y,z,"green")
x= [50,50]
y=[0,50]
z=[0,0]
ax.plot3D(x,y,z,"green")

x= [50,50]
y=[0,50]
z=[50,50]
ax.plot3D(x,y,z,"green")

x= [-10,-10]
y=[0,50]
z=[50,50]
ax.plot3D(x,y,z,"green")
ax.set_title("3D Shape")
plt.show()
   