'''
Created on Nov 13, 2016

@author: iskandar
'''



# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plot;
import matplotlib.image as mpimg;
 

def plot_image_array():
    
    img = mpimg.imread('images/stinkbug.png');
    
    
def hist_of_px():
    
    image = cv2.imread('images/bubu.jpg');
    plot.hist(image.ravel(), 256, [0,256]);
    plot.show();
        
def pseudocolor():
    
    img = mpimg.imread('images/stinkbug.png');
    limg = img[:, :, 0];
#    plot.imshow(limg);
    plot.colorbar();
    plot.hist(limg.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

def hist_rgb():
    
    image = cv2.imread("images/bubu.jpg");
    color = ('b', 'g', 'r');
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256]);
        plot.plot(histr, color = col);
        plot.xlim([0,256]);
    plot.show();

def crop_image(x1, x2, y1, y2):
    
    image = cv2.imread("images/bubu.jpg");
    cropped = image[x1:x2, y1:y2];
    cv2.imshow("cropped", cropped);
    cv2.waitKey(0);
    

def select_color_channel(channel):
    
    image = cv2.imread("images/bubu.jpg");
    cropped = image[:, :, channel];
    cv2.imshow("cropped", cropped);
    cv2.waitKey(0);

def color_channel_historgram(channel):
    
    image = cv2.imread("images/bubu.jpg", channel);
    plot.hist(image.ravel(), 256, [0, 256]);
    plot.show();
    
def add_images():
    
    image1 = cv2.imread("images/bubu.jpg");
    image2 = cv2.imread("images/dino.jpg");
    
    cv2.imshow("merged", image1/2 + image2/2);
    cv2.waitKey(0);
    

def scale_by_factor(factor):
    
    image = cv2.imread("images/bubu.jpg");
    
    cv2.imshow("scaled", image * factor);
    cv2.waitKey(0);

def gaussian_channel_noise():
    
    image = cv2.imread("images/dino.jpg");
    
    noise = np.zeros((480, 640), dtype=np.uint8);
    cv2.randn(noise, (0), (99));
    cv2.imshow("pic", image[:,:,2] + noise);
    cv2.waitKey(0);
    
    

if __name__ == '__main__':
    
    gaussian_noise();