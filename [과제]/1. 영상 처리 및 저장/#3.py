import cv2
import numpy as np

cap = cv2.VideoCapture('stopwatch.avi')
if not cap.isOpened():
    print("Video open failed!")
    exit()
    
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

delay = round(1000 / fps)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # int


outputVideo = cv2.VideoWriter('stopwatch_inv.avi', fourcc, fps, (w,h))
if not outputVideo.isOpened():
    print('File open failed!')
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    inversed = np.array(frame)
    if cap.get(cv2.CAP_PROP_POS_MSEC) >= 10000:
        inversed[h//2:, w//2:] = np.array(~frame)[h//2:, w//2:]
        
    outputVideo.write(inversed)
    
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    
    if cv2.waitKey(delay) == 27:
        break

cv2.destroyAllWindows()