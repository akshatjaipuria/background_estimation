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
cv2.imshow('frame', med_fr)
cv2.waitKey(0)