import os
from time import time
import cv2
from window_cap import WindowCapture

wincap = WindowCapture('project-CV-RES')

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    cv2.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1/(time()-loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done')

