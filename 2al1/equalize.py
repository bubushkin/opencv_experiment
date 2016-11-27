'''
Created on Nov 24, 2016

@author: iskandar
'''


from __future__ import print_function;
import numpy as np;
import cv2;
from matplotlib import pyplot as plt;


image = cv2.imread('images/ocean.jpg');

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

cv2.imshow("original", image);


hist = cv2.calcHist([image], [0], None, [256], [0, 256]);


plt.figure();
plt.title("Grayscale histogram");
plt.xlabel("Bins");
plt.ylabel("# of Pixels");
plt.plot(hist);
plt.xlim([0,256]);
plt.show();

eq = cv2.equalizeHist(image);

cv2.imshow("histogram equlized", np.hstack([image, eq]));

hist = cv2.calcHist([eq], [0], None, [256], [0, 256]);


plt.figure();
plt.title("Equalized histogram");
plt.xlabel("Bins");
plt.ylabel("# of Pixels");
plt.plot(hist);
plt.xlim([0,256]);
plt.show();




cv2.waitKey(0);