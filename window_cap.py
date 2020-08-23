import numpy as np
import win32gui, win32ui, win32con

class WindowCapture:
    # Properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

 
    # Constructor
    def __init__(self, window_name): 

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            ## CALL GAME END FUNCTION HERE TO INITATE LOOP
            raise ValueError('Window not found: {}'.format(window_name))


        # Defining monitor width and height
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # Removing window borders
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels*2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # save screenshot
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h,self.w,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # Dropping Alpha-channel
        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

    def get_screen_position(self):
        return [self.offset_x, self.offset_y, self.w,self.h]
