import cv2
import tensorflow as tf
from data_processing import data_tools

import os
from time import sleep
from time import time
import cv2
from window_cap import WindowCapture
from vision_adjust import VisionAdjust
from hsvfilter import HsvFilter
from pynput.mouse import Button, Controller

# Note: Neural Net reponse images placed after image 5380

mouse = Controller()

CATEGORIES = ['wait', 'shoot']

# img=data_tools().data_img_read_test(filepath='images/just missed/3642.jpg')

model=tf.keras.models.load_model('32x4_v2-CNN.model')

wincap = WindowCapture('VALORANT  ')
selected_vision = VisionAdjust()
# new_vision = selected_vision.init_control_gui()

hsv_filter = HsvFilter(0,141,0,179,255,255,0,0,0,0)
y = 442
x = 898
width = 104
height = 169

count=8058

loop_time = time()

while(True):
    screenshot = wincap.get_screenshot()
    crop_img = screenshot[y:y+height, x:x+width]
    output_image_og = selected_vision.apply_hsv_filter(crop_img, hsv_filter)
    output_image = output_image_og.reshape(-1, 104, 169, 3)
    prediction=model.predict([output_image])
    response=CATEGORIES[int(prediction[0][0])]
    if response=='shoot':
        mouse.click(Button.left, 1)
        cv2.imwrite('images/test/{}_r.jpg'.format(count), crop_img)
        cv2.imwrite('images/test/{}.jpg'.format(count), output_image_og)
        print(count)
        count+=1
    
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()
