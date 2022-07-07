import face_alignment
import cv2
import numpy as np
import torch
from skimage import io
import matplotlib.pyplot as plt

#inputing video
cap = cv2.VideoCapture('brianvid1.mp4')

#Accumulating all the frames in the video to get the total 
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#Creating the window for the video output 
cv2.namedWindow('frame',0)
cv2.resizeWindow('frame',300,300)

# choose codec according to format needed, size, and put it together with the frames per second
# to compose the format of the video
framesize = (300,300)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
video = cv2.VideoWriter('output.avi', fourcc, 20, framesize) #the third one represents frames per second

# Sets up the facial recognition package 
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', face_detector='sfd') # 'cpu' for cpu, 'cuda' for gpu
frames = []

# adjusting size and color of points on the face 
radius = 3
color = (100, 200, 200)
color2 = (200, 0, 0)
thickness = -1

# Functions to average the middle of the mouth 
def avga(i,a,b):

    for i in range(0,12): 
            a = a + mouth_points[i,0]
            b = b + mouth_points[i,1]
            avga = a/12
            avgb = b/12 
    return avga 

def avgb(i,a,b):

    for i in range(0,12): 
            a = a + mouth_points[i,0]
            b = b + mouth_points[i,1]
            avga = a/12
            avgb = b/12 

    return avgb 


#function that shows points on face 
def show_points(Points, frame):
    for point in Points:
        frame = cv2.circle(frame, tuple(point), radius, color, thickness)

    return frame

# While loop that puts the frames together 
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    frames.append(frame)
    i+=1

# This will have loop run through the mouth markers for every frame
for i in range(0,length):
    if frames[i] is not None:
        det = fa.get_landmarks(frames[i])

        if det is not None:
            Points = det[-1].astype(int)
            # coordinates of the mouth, both columns and elements 48-60
            mouth_points = Points[48:60, :] 
            #actually puts the points on the face 
            frames[i] = show_points(mouth_points, frames[i])

            # Making the circle in the middle of the mouth coordinates x and y
            cv2.circle(frames[i], (int(avga(0,0,0)),int(avgb(0,0,0))), radius, color2, thickness)


            # Output each frame as a jpg image 
            # img = cv2.imwrite('test'+str(i)+'.jpg',frames[i]) # equal it to something 

            #preparing  videooutput with the necessary frame size and writing it
            vidout=cv2.resize(frames[i],(300,300))
            video.write(vidout)

            #showing a popup window with each frame
            cv2.imshow('frame',frames[i])

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break        

#Display the resulting frames
video.release()    
cap.release()
cv2.destroyAllWindows()

