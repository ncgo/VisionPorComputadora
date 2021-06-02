# import dependencies
from base64 import b64decode, b64encode
import cv2
import numpy as np
import PIL
import io
import time
import matplotlib.pyplot as plt

WINDOW_WIDTH    = 640
WINDOW_HEIGHT   = 480

# cap = cv2.VideoCapture(0)
# cap.set(3,WINDOW_WIDTH)     #width=640
# cap.set(4,WINDOW_HEIGHT)    #height=480

# mouseX = 0
# mouseY = 0
# flag = True

# def detectClick(event,x,y,flags,param):
#     global mouseX,mouseY,flag
#     if event == cv2.EVENT_LBUTTONDOWN:
#         mouseX,mouseY = x,y
#         flag = False

# cv2.namedWindow('video_feed')
# cv2.setMouseCallback('video_feed',detectClick)

# frame = None

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     # Display the resulting frame
#     cv2.imshow('video_feed',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     if not flag:
#         break

# cap.release()

image = cv2.imread("./person.jpg")

window_name = 'image'

cv2.imshow(window_name, image)
  
#waits for user to press any key 
cv2.waitKey(0) 

cv2.destroyAllWindows()