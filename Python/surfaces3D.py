from matplotlib.collections import PolyCollection
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(2,4,1,projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')

ax=fig.add_subplot(2,4,2,projection="3d")
x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a*a + Y*Y/b*b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Elliptic Paraboloid')
r=1
u=np.linspace(-2,2,200)
v=np.linspace(0,2*np.pi,60)
[u,v]=np.meshgrid(u,v)
ax=fig.add_subplot(2,4,3,projection="3d")
a,b,c = 1, 1, 1
x = a*np.cosh(u)*np.cos(v)
y = b*np.cosh(u)*np.sin(v)
z = c*np.sinh(u)
# x = np.linspace(-20, 20, 30)
# y = np.linspace(-20, 20, 30) 
# X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y

# Z = np.sqrt((c*c)*((X*X/a*a + Y*Y/b*b)-1))    
# Z2= -np.sqrt((c*c)*((X*X/a*a + Y*Y/b*b)-1))     # make a 2D array and assign it to Z
ax.plot_surface(x,y,z,rstride=4,cstride=4)
# ax.contour3D(X,Y,Z2,200)
ax.set_title('Hyperbolic Hyperboloid') 
ax = fig.add_subplot(2,4,4,projection='3d')
x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
Z = np.sqrt((c*c)*((X*X/a*a + Y*Y/b*b)+1))    
Z2= -np.sqrt((c*c)*((X*X/a*a + Y*Y/b*b)+1)) 
ax.contour3D(X,Y,Z,100)    # make a 2D array and assign it to Z
ax.contour3D(X,Y,Z2,100)
ax.set_title('Elliptic Hyperboloid')
ax=fig.add_subplot(2,4,5,projection="3d")
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")
ax.set_title('Sphere')
ax=fig.add_subplot(2,4,6,projection="3d")
u, v = np.mgrid[0:2*np.pi:80j, 0:np.pi:80j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.sqrt(x**2 + y**2)
ax.plot_surface(x,y,z)
ax.set_title('Cone')
ax=fig.add_subplot(2,4,7,projection="3d")
Pyramid = np.zeros([512, 512])
x = Pyramid.shape[0]
y = Pyramid.shape[1]

for i in range(x // 2):
    for j in range(i, x - i):
        for h in range(i, x - i):
            Pyramid[j, h] = i
x2d, y2d = np.meshgrid(range(x), range(y))
ax.plot_surface(x2d, y2d, Pyramid)

ax.set_title('pyramid')
ax=fig.add_subplot(2,4,8,projection="3d")
cube=np.zeros([512,512])
x=cube.shape[0]
y=cube.shape[1]
for i in range(x):
    for j in range(i):
        for h in range(i):
            cube[j,h]=i
x2d,y2d=np.meshgrid(range(x),range(y))
ax.plot_surface(x2d,y2d,cube,color="b")
ax.plot_surface(y2d,-x2d,cube,color="b")

ax.set_title("Parallelepiped")
plt.show()