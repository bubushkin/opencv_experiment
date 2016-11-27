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


#cv2.line(canvas, (0, 0), (300, 300), red);

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2);



for (col, c) in enumerate(range(0, 300, 10)):
    for (row, r) in enumerate(range(0, 300, 10)):

        fill = (0, 255, 0);
        
        if( col % 2 == row % 2):
            fill = (0, 0, 0);
        
        cv2.rectangle(canvas, (c, r), (c+10, r+10), fill, -1);


cv2.circle(canvas, (centerX, centerY), 30, red, -1);

cv2.imshow("Canvas", canvas);


cv2.waitKey(0);
