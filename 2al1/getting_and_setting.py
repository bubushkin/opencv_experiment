'''
Created on Nov 24, 2016

@author: iskandar
'''

from __future__ import print_function;
from argparse import ArgumentParser;
import cv2;



ap = ArgumentParser();
ap.add_argument("-i", "--image", required=True, help="Path to the image");
args = vars(ap.parse_args());


im = cv2.imread(args["image"]);

print("width: {} pixels".format(im.shape[1]));
print("height: {} pixels".format(im.shape[0]));
print("channels: {}".format(im.shape[2]));


cv2.imshow("Original", im);

b, g, r = im[0, 0];

print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b));

im[0, 0] = (0, 0, 255);
b, g, r = im[0, 0];
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b));

corner = im[0:100, 0:100];
cv2.imshow("Corner", corner);

im[0:100, 0:100] = (255,0,0);

cv2.imshow("modified", im);

cv2.waitKey(0);
