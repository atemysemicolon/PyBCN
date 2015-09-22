# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:19:55 2015

@author: prassanna
"""

from sklearn import datasets, svm, metrics
import matplotlib.pyplot as plt
import numpy as np

digits = datasets.load_digits()
images = digits.images
labels = digits.target


def disp_images(images,labels,nr_disp =4, mode="Training"):
    fig = plt.figure()
    ax = fig.add_subplot(1,nr_disp,1)

    for index in range(0,nr_disp):
        plt.subplot(1, nr_disp, index + 1)
        plt.imshow(images[index], cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title(mode + ': %i' % labels[index])
    return None



disp_images(images,labels)

n_samples = len(images)
data = images.reshape((n_samples,-1))
#print data[0]


classifier = svm.SVC(gamma=0.001)
#First half to train
#Second half to test
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])


predicted = classifier.predict(data[n_samples / 2:])
expected = digits.target[n_samples / 2:]

disp_images(images[n_samples/2 : ],predicted,nr_disp=15,mode="Testing")


true_positives= np.count_nonzero(expected==predicted)
acc = float(true_positives) / len(expected)
print "Classifier Accuracy is ",acc