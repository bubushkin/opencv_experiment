'''
Created on Nov 27, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;



image = cv2.imread('images/coins.jpg');

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
cv2.imshow("original", image);


blurred = cv2.GaussianBlur(image, (5, 5), 0);

(T, threshold) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY);
cv2.imshow("threshold image", threshold);

(T, inv_threshold) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV);
cv2.imshow("invthreshold", inv_threshold);

cv2.imshow("coins", cv2.bitwise_and(image, image, mask = inv_threshold));

cv2.waitKey(0);