import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
l, = ax.plot(x, 3*x*np.tan(x/2))
def animate(j):
    l.set_ydata(3*x*np.tan(x + j / 50)) 
    return l,
ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)
plt.title("Weird Heartbeat Monitor")
plt.show()
