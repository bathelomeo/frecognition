from types import FrameType
import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('m'):
        break
    cv2.imshow('SIRs CAM', frame)
