import numpy as np
import matplotlib.pyplot as plt
def cylinder(radius, height):
    fig = plt.figure(tight_layout=True)
    ax = plt.axes(projection='3d')
    theta=np.linspace(0, 2*np.pi, 50)
    Z=np.linspace(0,height,50)
    t,zed=np.meshgrid(theta,Z)
    x=radius*np.cos(theta)
    y=radius*np.sin(theta)
    X,Y= np.meshgrid(x, y)
    ax.plot3D(X,Y,zed,50)
    plt.show()


if __name__ == '__main__':
    cylinder(1, 2)
    cylinder(2, 10)