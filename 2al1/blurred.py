'''
Created on Nov 24, 2016

@author: iskandar
'''


from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;



image = cv2.imread('images/ocean.jpg');

blurred = np.hstack([cv2.blur(image, (3,3)), cv2.blur(image, (5,5)), cv2.blur(image, (7,7))]);
cv2.imshow("averaged", blurred);

blurred = np.hstack([cv2.GaussianBlur(image, (3,3), 0), cv2.GaussianBlur(image, (5,5), 0), cv2.GaussianBlur(image, (7,7), 0)]);
cv2.imshow("gaussian", blurred);

blurred = np.hstack([cv2.medianBlur(image, 3), cv2.medianBlur(image, 5), cv2.medianBlur(image, 7)]);
cv2.imshow("median", blurred);


blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21), cv2.bilateralFilter(image, 7, 31, 31), cv2.bilateralFilter(image, 9, 41, 41)]);
cv2.imshow("bilateral", blurred);


cv2.waitKey(0);

