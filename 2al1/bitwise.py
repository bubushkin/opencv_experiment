'''
Created on Nov 24, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
from argparse import ArgumentParser;
import cv2;


rect = np.zeros((300, 300), dtype='uint8');
cv2.rectangle(rect, (25, 25), (275, 275), 255, -1);

cv2.imshow("rect", rect);

circ = np.zeros((300, 300), dtype='uint8');
cv2.circle(circ, (150,150), 150, 255, -1);

cv2.imshow("circ", circ);


bitwiseAnd = cv2.bitwise_and(rect, circ);
cv2.imshow("and", bitwiseAnd);


bitwiseOr = cv2.bitwise_or(rect, circ);
cv2.imshow("OR", bitwiseOr);

bitwiseXor = cv2.bitwise_xor(rect, circ);
cv2.imshow("xor", bitwiseXor);

bitwiseNot = cv2.bitwise_not(rect, circ);
cv2.imshow("not", bitwiseNot);


cv2.waitKey(0);