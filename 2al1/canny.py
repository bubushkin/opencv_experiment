'''
Created on Nov 27, 2016

@author: iskandar
'''

from __future__ import print_function;
import cv2;
import mahotas;




image = cv2.imread('images/coins.jpg');

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
cv2.imshow("original", image);

image = cv2.GaussianBlur(image, (5, 5), 0);

canny = cv2.Canny(image, 30, 150);
cv2.imshow("canny", canny);
cv2.waitKey(0);
