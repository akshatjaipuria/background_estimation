import cv2
import numpy as np
vid = cv2.VideoCapture('clip.mp4')

fids = vid.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size = 50)

frames = []
for fid in fids :
    vid.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = vid.read()
    frames.append(frame)

med_fr = np.median(frames, axis = 0).astype(dtype = np.uint8)

vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

med_fr_gr = cv2.cvtColor(med_fr, cv2.COLOR_BGR2GRAY)

flag = True

while(flag):
    flag, frame = vid.read()
    if flag == False:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(frame, med_fr_gr)

    th, diff = cv2.threshold(diff, 35, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame', diff)
    cv2.waitKey(20)

vid.release()
cv2.destroyAllWindows()