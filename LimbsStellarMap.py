#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt


# In[28]:


# create some 1D arrays
x1d = np.linspace(-1, 1, 100)
y1d = np.linspace(-1, 1, 100)

# create 2D arrays of x and y
x2d, y2d = np.meshgrid(x1d, y1d)


# In[42]:


def intensity_imshow(c1, c2, title):
    '''
    This function is a help to demonstrate how
    imshow-ing arrays works in matplotlib.
    '''
    
    # create a new figure
    plt.figure(figsize=(10,4), dpi=300)
    
      # intensity equation for quadratic limb darkening
    x_limb_darkening = np.sqrt(x2d**2 + y2d**2)
    mu = np.sqrt(1 - (x_limb_darkening**2))
    I = (1 - c1*(1-mu) - c2*(1-mu)**2)
    offstar = x_limb_darkening > 1
    I[offstar] = 0
    
    # make an image, with brightness representing array values
    plt.imshow(I, 
               cmap='gray', # Choose the color map.
               origin='lower', # Set (x,y) = (0,0) to be the lower left.
               extent=[np.min(x1d), # Extent sets the coordinates for the corners
                       np.max(x1d), #  of the array you're plotting
                       np.min(y1d), #  [left, right, bottom, top]
                       np.max(y1d)],
               aspect='equal', # How is the aspect ratio of the plot set?
               interpolation='nearest') # How are points visually interpolated?
    

    
    # add a colorbar indicating the scale of the colors
    plt.colorbar(label=title)

    # plot labels
    plt.xlabel('x (stellar radii)')
    plt.ylabel('y (stellar radii)')
    plt.title(title)



