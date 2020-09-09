import os
from time import sleep
from time import time
import cv2
from window_cap import WindowCapture
from vision_adjust import VisionAdjust
from hsvfilter import HsvFilter
import win32api

wincap = WindowCapture('VALORANT  ')
selected_vision = VisionAdjust()
# new_vision = selected_vision.init_control_gui()

hsv_filter = HsvFilter(0,141,0,179,255,255,0,0,0,0)
y = 442
x = 898
width = 104
height = 169

loop_time = time()

state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)
count = 9515

while(True):

    # cv2.imwrite('test.jpg', screenshot)
    a = win32api.GetKeyState(0x01) 
    b = win32api.GetKeyState(0x02) 
 
    if a != state_left:  # Button state changed 
        state_left = a 
        # print(a) 
        if a < 0: 
            print('Left Button Pressed') 
            screenshot = wincap.get_screenshot()
            crop_img = screenshot[y:y+height, x:x+width]
            output_image = selected_vision.apply_hsv_filter(crop_img, hsv_filter)
            cv2.imwrite('images/positive/{}_r.jpg'.format(count), crop_img)
            cv2.imwrite('images/positive/{}.jpg'.format(count), output_image)
            print(count)
            count += 1
        else: 
            print('Left Button Released') 
 
    # if b != state_right:  # Button state changed 
    #     state_right = b 
    #     # print(b) 
    #     if b < 0: 
    #         print('Right Button Pressed') 
    #     else: 
    #         print('Right Button Released') 
    loop_time = time()

    sleep(0.001) 
    
    
    # cv2.imshow('Computer Vision', output_image)

    # print('FPS {}'.format(1/(time()-loop_time)))

    # if cv2.waitKey(1) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break

print('Done')

