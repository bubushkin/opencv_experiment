'''
Created on Nov 24, 2016

@author: iskandar
'''



from __future__ import print_function;
import numpy as np;
from argparse import ArgumentParser;
import cv2;



image = cv2.imread('images/dino.jpg');

mask = np.zeros(image.shape[:2], dtype='uint8');


(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2);
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1);

masked = cv2.bitwise_and(image, image, mask = mask);
cv2.imshow("masked", masked);

cv2.waitKey(0);