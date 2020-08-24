import os
from time import time
import cv2
from window_cap import WindowCapture
from vision_adjust import VisionAdjust
from hsvfilter import HsvFilter

wincap = WindowCapture('VALORANT  ')
selected_vision = VisionAdjust()
new_vision = selected_vision.init_control_gui()

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    output_image = selected_vision.apply_hsv_filter(screenshot)
    cv2.imshow('Computer Vision', output_image)

    print('FPS {}'.format(1/(time()-loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done')

