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





blurred = cv2.GaussianBlur(image, (5, 5), 0);

T = mahotas.thresholding.otsu(blurred);

print("OTSU T level: {}".format(T));

threshold = image.copy();
threshold[threshold > T] = 255;
threshold[threshold < 255] = 0;

threshold = cv2.bitwise_not(threshold);
cv2.imshow("OTSU IMAGE", threshold);


T = mahotas.thresholding.rc(blurred);
print("RIDDLE-CALVARD T level: {}".format(T));

threshold = image.copy();
threshold[threshold > T] = 255;
threshold[threshold < 255] = 0;
threshold = cv2.bitwise_not(threshold);
cv2.imshow("RIDDLE-CALVARD", threshold);

cv2.waitKey(0);
