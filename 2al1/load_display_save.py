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


cv2.imshow("dino", im);

cv2.waitKey(0);

cv2.imwrite("/tmp/newimage.jpg", im);