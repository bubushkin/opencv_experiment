'''
Created on Nov 24, 2016

@author: iskandar

'''

import numpy as np;
import cv2;

canvas = np.zeros((300, 300, 3), dtype="uint8");

green = (0, 255, 0);
red = (0, 0, 255);
blue = (255, 0, 0);


cv2.line(canvas, (0, 0), (300, 300), green, 5);
cv2.line(canvas, (300, 0), (0, 300), red);

cv2.rectangle(canvas, (10, 10), (80, 80), green, -20);
cv2.rectangle(canvas, (100, 240), (140, 400), blue);



(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2);
white = (255, 255, 255);

for x in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), x, white);


cv2.imshow("Canvas", canvas);

canvas2 = np.zeros((300, 300, 3), dtype="uint8");


for x in range(0, 25):
    radius = np.random.randint(5, high=200);
    color = np.random.randint(0, high=256, size=(3,)).tolist();
    
    pt = np.random.randint(0, high=300, size=(2,));
    cv2.circle(canvas2, tuple(pt), radius, color, -1);
    

cv2.imshow("abstaction", canvas2);
cv2.waitKey(0);
