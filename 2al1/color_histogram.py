'''
Created on Nov 24, 2016

@author: iskandar
'''


from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;


image = cv2.imread('images/ocean.jpg');


chans = cv2.split(image);

colors = ('b', 'g', 'r');

plt.figure();
plt.title("Flattened color histogram");
plt.xlabel('Bins');
plt.ylabel("# of Pixels");

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256]);
    plt.plot(hist, color = color);
    plt.xlim([0, 256]);


plt.show();
cv2.waitKey(0);