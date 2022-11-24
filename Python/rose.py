from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,2*np.pi,10000)
def param(t,n,d):
    x=np.cos((n/d)*t)*np.cos(t)
    y=np.cos((n/d)*t)*np.sin(t)
    return [t,x,y]
In=2
Id=1
fig,ax=plt.subplots()
arr=param(t,In,Id) 
l,=ax.plot(param(t,In,Id)[1],param(t,In,Id)[2])
fig.subplots_adjust(left=0.25,bottom=0.25)
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
Sn=Slider(ax=axfreq,label='N',valmin=1,valmax=7,valstep=1,valinit=In,)
Sd=Slider(ax=axamp,label="D",valmin=1,valmax=9,valstep=1,valinit=Id,orientation="vertical",)
def update(val):
    t0=val
    t=np.linspace(0,2*np.pi,10000)
    ax.clear()
    for i in range(round(Sd.val)):
        t=np.linspace(2*(i)*np.pi,2*(i+1)*np.pi,10000)
        ax.plot(param(t,Sn.val,Sd.val)[1], param(t,Sn.val,Sd.val)[2])
    fig.canvas.draw()
Sn.on_changed(update)
Sd.on_changed(update)
plt.grid()
plt.show()

