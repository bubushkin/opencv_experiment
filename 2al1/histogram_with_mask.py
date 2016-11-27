'''
Created on Nov 24, 2016

@author: iskandar
'''


from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;



def plot_histogram(image, title, mask=None):
    
    chans = cv2.split(image);
    colors = ('b', 'g', 'r');
    
    plt.figure();
    plt.title(title);
    plt.xlabel('Bins');
    plt.ylabel('pixels');
    
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256]);
        plt.plot(hist, color = color);
        plt.xlim([0, 256]);
    plt.show();
        

image = cv2.imread('images/ocean.jpg');

mask = np.zeros(image.shape[:2], dtype='uint8');
cv2.rectangle(mask, (15,15), (130, 100), 255, -1);
cv2.imshow('mask', mask);

masked = cv2.bitwise_and(image, image, mask=mask);
cv2.imshow("Masked", masked);

plot_histogram(image, "histogram for masked region", mask);

cv2.waitKey(0);

