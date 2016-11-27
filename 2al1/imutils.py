'''
Created on Nov 24, 2016

@author: iskandar
'''

import numpy as np;
import cv2;


def translate(image, x, y):
    matrix = np.float32([[0x01, 0x0, x ],[0x0, 0x01, y]]);
    return cv2.warpAffine(image, matrix, (image.shape[0x01], image.shape[0x0]));

def rotate(image, deg, center=None, scale=1.0):
    (height, width) = image.shape[:2];
    
    if(center is None):
        center = (width // 2, height // 2);
    
    matrix = cv2.getRotationMatrix2D(center, deg, scale);
    return cv2.warpAffine(image, matrix, (width, height));

def resize(image, size, type='w'):
    
    ration = None;
    dim = None;
    
    if(type == 'w'):
        ratio = size / image.shape[1];
        dim = (int(size), int(image.shape[0] * ratio));

    else:
        ratio = size / image.shape[0];
        dim = (int(image.shape[0] * ratio), int(size));
    
    return cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR);
    
def flip(image, direction):
    
    return cv2.flip(image, direction);
    
def crop(image, starty, endy, startx, endx):
    return image[starty:endy, startx:endy];
        
