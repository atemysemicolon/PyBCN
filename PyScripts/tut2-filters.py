# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:10:04 2015

@author: prassanna
"""

###FILTERS AND BLURRING############

from skimage import filter,io,data,color,feature,img_as_float
from matplotlib import pyplot as plt
import numpy as np

img = img_as_float(data.checkerboard());
print img.shape
io.imshow(img)

##Gaussian
noisy = img + 0.6 * img.std() * np.random.random(img.shape)
noisy = np.clip(noisy, 0, 1)
blurred = filter.gaussian_filter(noisy, 2);
#blurred_int = np.uint8(blurred*255)
#print np.amax(blurred_int)
bla = np.vstack((img,noisy,blurred))
io.imshow(bla)


#2nd Gaussian
from math import sqrt
img_2  = data.hubble_deep_field()
img_2  = img_2 [0:500,0:500]
io.imshow(img_2)
img_gray = color.rgb2gray(img_2)

blobs_log = feature.blob_log(img_gray, max_sigma=30, num_sigma=10, threshold=.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

blobs_dog = feature.blob_dog(img_gray, max_sigma=30, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)


def disp_blob(blobs,title):
    fig, ax = plt.subplots(1,1)
    ax.set_title(title)    
    ax.imshow(img_2, interpolation='nearest')
       

    for blob in blobs:        
        y, x, r = blob
        c = plt.Circle((x, y), r, color='yellow', linewidth=2, fill=False)
        ax.add_patch(c)

    return None
    
disp_blob(blobs_log,"LoG");
disp_blob(blobs_dog, "DoG");