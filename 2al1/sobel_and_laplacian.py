'''
Created on Nov 27, 2016

@author: iskandar
'''

from __future__ import print_function;
import cv2;
import numpy as np;




image = cv2.imread('images/coins.jpg');

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

lap = cv2.Laplacian(image, cv2.CV_64F);

lap = np.uint8(np.absolute(lap));

cv2.imshow("laplacian", lap);

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0);
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1);

sobelX = np.uint8(np.absolute(sobelX));
sobelY = np.uint8(np.absolute(sobelY));

sobelCombined = cv2.bitwise_or(sobelX, sobelY);
cv2.imshow("Sobel X", sobelX);
cv2.imshow("Sobel Y", sobelY);
cv2.imshow("Sobel Combined", sobelCombined);



cv2.waitKey(0);