'''
Created on Nov 24, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
from argparse import ArgumentParser;
import cv2;


ap = ArgumentParser();
ap.add_argument("-i", "--image", required=True, help="Path to image");
args = vars(ap.parse_args());

im = cv2.imread(args['image']);

cv2.imshow("Original", im);

matrix = np.ones(im.shape, dtype="uint8") * 100;
added = cv2.add(im, matrix);

cv2.imshow("added", added);

matrix = np.ones(im.shape, dtype="uint8") * 50;
subtracted = cv2.subtract(im, matrix);

cv2.imshow("subtracted", subtracted);


cv2.waitKey(0);