'''
Created on Nov 27, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;
from logging import thread



image = cv2.imread('images/coins.jpg');

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
cv2.imshow("original", image);


blurred = cv2.GaussianBlur(image, (5, 5), 0);

threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4);
cv2.imshow("Mean thresh", threshold);


threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3);
cv2.imshow("gaussian thresh", threshold);


cv2.waitKey(0);