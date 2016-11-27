'''
Created on Nov 24, 2016

@author: iskandar
'''


from __future__ import print_function;
import numpy as np;
import cv2;


image = cv2.imread('images/ocean.jpg');
(B, G, R) = cv2.split(image);

cv2.imshow("Blue", B);
cv2.imshow("Green", G);
cv2.imshow("Red", R);

cv2.waitKey(0);

merged = cv2.merge([B,G,R]);
cv2.imshow("merged", merged);
cv2.waitKey(0);

zeros = np.zeros(image.shape[:2], dtype='uint8');
cv2.imshow("Red", cv2.merge([zeros, zeros, R]));
cv2.imshow("Green", cv2.merge([zeros, G, zeros]));
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]));

cv2.waitKey(0);


cv2.destroyAllWindows();

