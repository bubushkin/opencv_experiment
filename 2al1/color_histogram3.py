'''
Created on Nov 25, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;


image = cv2.imread('images/ocean.jpg');



fig = plt.figure();


chans = cv2.split(image);


hist = cv2.calcHist([image], [0, 1, 2], None, [8,8,8], [0, 256, 0, 256, 0, 256]);
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]));

plt.show();
