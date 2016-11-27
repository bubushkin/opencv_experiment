'''
Created on Nov 24, 2016

@author: iskandar
'''

import numpy as np;
from argparse import ArgumentParser;
from imutils import translate, rotate, resize, flip, crop;
import cv2;


ap = ArgumentParser();
ap.add_argument("-i", "--image", required=True, help="Path to image");

args = vars(ap.parse_args());

im = cv2.imread("images/dino.jpg");

cv2.imshow("Original", translate(im, 50, 100));


cv2.imshow("Rotated", rotate(im, -50));

cv2.imshow("Resized", resize(im, 300.0, 'h'));

cv2.imshow("Resized", flip(im, 0));


cv2.imshow("Resized", crop(im, 50, 150, 100, 210));


cv2.waitKey(0);