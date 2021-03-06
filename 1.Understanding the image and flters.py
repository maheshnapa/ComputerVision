# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:56:35 2020

@author: Mahesh Napa
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = io.imread('./data/lena.jpg')

plt.imshow(img)
plt.show()

print(img.shape)


# Split the channels
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

plt.imshow(red, cmap="Reds")
plt.show()

plt.imshow(green, cmap="Greens")
plt.show()

plt.imshow(blue, cmap="Blues")
plt.show()

def filtering(img, f=3):
    
    # Dimensions from the input shape
    (rows, col, channels) = img.shape
    
    # Initialize "hyper parameters"
    stride = 2
    
    # Dimensions of the output
    n_rows = int(1 + (rows - f) / stride)
    n_col = int(1 + (col - f) / stride)
    n_channels = channels
    
    # Initialize output matrix A
    n_img = np.zeros((n_rows, n_col, n_channels))              
    
    # iterate through img
    for h in range(n_rows):                     
        for w in range(n_col):                 
            for c in range (n_channels):            
                vert_start = h*stride
                vert_end = vert_start + f
                horiz_start = w*stride
                horiz_end = horiz_start + f

                # extract slice we are dealing with
                n_slice = img[vert_start:vert_end, horiz_start:horiz_end, c]

                # Compute the filtering operation on the slice
                n_img[h, w, c] = np.mean(n_slice, dtype=int)
    return n_img

A = filtering(img)
print A.shape
plt.imshow(A)
plt.show()

A = filtering(img, f=11)
print A.shape
plt.imshow(A)
plt.show()

A = filtering(img, f=25)
print A.shape
plt.imshow(A)
plt.show()