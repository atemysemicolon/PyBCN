# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:50:18 2015

@author: prassanna
"""

from skimage import io,data,color
import numpy as np


img = data.astronaut();
#io.imshow(img)


blaR = img[:,:,0]
blaG = img[:,:,1]
blaB = img[:,:,2]

bla = np.vstack((blaR,blaG, blaB))
#io.imshow(bla)

print np.amax(blaR), np.amax(blaG), np.amax(blaB)
#io.imshow(img)

mask  = blaR>128;
#io.imshow(mask)
img_gray = color.rgb2gray(img);
img_gray[mask] = 128;
io.imshow(img_gray)
