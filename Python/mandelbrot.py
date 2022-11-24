import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mandelbrot( h,w, maxiter=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x,y = np.ogrid[ -2.7:0.8:0.5*h*1j, -1.4:1.4:0.5*w*1j ]     # make two vectors x and y  
    c = x+y*1j                                       # make a 2D array of complex numbers
    z = c
    divtime = maxiter + np.zeros(z.shape, dtype=int) # make a pixel map

    for i in range(maxiter):
        z = z**2 + c                            # update z, the 2D array of complex numbers
        diverge = z*np.conj(z) > 2**2           # find all diverging points, diverge is a Boolean 2D array
        div_now = diverge & (divtime==maxiter)  # find now diverging points
        divtime[div_now] = i                    # update the pixel map
        z[diverge] = 2                          # avoid diverging too much

    return divtime

img = mandelbrot(400,400)
im= mpimg.imread('mandelbrot.png')
plt.imsave("mandelbrot.png", img)
lum_img=im[:,:,0]
plt.imshow(lum_img,cmap="hot")    

plt.show()