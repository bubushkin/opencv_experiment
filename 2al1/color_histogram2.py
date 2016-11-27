'''
Created on Nov 25, 2016

@author: iskandar
'''

from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;


image = cv2.imread('images/ocean.jpg');



fig = plt.figure();


chans = cv2.split(image);


ax = fig.add_subplot(131);
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256]);
p = ax.imshow(hist, interpolation = "nearest");
ax.set_title("2D Color histogram for G and B");
plt.colorbar(p);


ax = fig.add_subplot(132);
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256]);
p = ax.imshow(hist, interpolation = "nearest");
ax.set_title("2D Color histogram for G and R");
plt.colorbar(p);


ax = fig.add_subplot(133);
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256]);
p = ax.imshow(hist, interpolation = "nearest");
ax.set_title("2D Color histogram for B and R");
plt.colorbar(p);

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]));

hist = cv2.calcHist([image], [0, 1, 2], None, [8,8,8], [0, 256, 0, 256, 0, 256]);
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]));

plt.show();
