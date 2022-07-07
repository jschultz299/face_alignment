import face_alignment
import cv2
import numpy as np
import torch
from skimage import io
import matplotlib.pyplot as plt
import math

#inputing video
cap = cv2.VideoCapture('brianvid1.mp4')

#Accumulating all the frames in the video to get the total 
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)


#parameters for middle ellipse
radius = 5
radius2 = 10
radiuscenter = 60
color = (100, 200, 200)
color2 = (200, 0, 0)
colorcenter = (0,200,0)
thickness = -1
windmidthick = 2

#parameters for the arrow
arrowcolor = (0,50,200)
arrowthickness = 2

#parameters for text 
coordinatestext1 = (100,600)
coordinatestext2 = (100,640)
coordinatestext3 = (100,680)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
colortext = (255,0,255)
thicknesstext = 2


#Creating the window for the video output 
cv2.namedWindow('frame',0)
cv2.resizeWindow('frame',300,300)

# choose codec according to format needed, size, and put it together with the frames per second
# to compose the format of the video
framesize = (300,300)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
video = cv2.VideoWriter('regularvid.avi', fourcc, 20, framesize) #the third one represents frames per second

# Sets up the facial recognition package 
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', face_detector='sfd') # 'cpu' for cpu, 'cuda' for gpu
frames = []

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

for i in range(0,length):
    if frames[i] is not None:
        det = fa.get_landmarks(frames[i])

        if det is not None:
            Points = det[-1].astype(int)
            # coordinates of the mouth, both columns and elements 48-60
            mouth_points = Points[48:60, :] 
            #actually puts the points on the face 
            frames[i] = show_points(mouth_points, frames[i])

            windwidth = int(width/2)
            windheight = int(height/2) 

            mouthwidth = int(avga(0,0,0))
            mouthheight = int(avgb(0,0,0))

            arrow = cv2.arrowedLine(frames[i], (windwidth,windheight),(mouthwidth,mouthheight), arrowcolor, arrowthickness)

            # Making the center of window 
            windmid = cv2.circle(frames[i],(windwidth,windheight), radiuscenter, colorcenter, windmidthick)

            # Making the circle in the middle of the mouth coordinates x and y
            mouthmid = cv2.circle(frames[i], (mouthwidth,mouthheight), radius2, color2, thickness)

            d = math.sqrt(pow((mouthwidth-windwidth),2)+ pow((mouthheight-windheight),2))
            
            text1comment = "Distance: " + str(round(d))

            text2comment = "Distance x and y: " + "(" + str(abs(windwidth-mouthwidth)) + " , " + str(abs(windheight-mouthheight)) + ")"

            # making text for distance of window and mouth
            text1 = cv2.putText(frames[i], text1comment, coordinatestext1, font, fontScale, colortext, thicknesstext, cv2.LINE_AA)
            text2 = cv2.putText(frames[i], text2comment, coordinatestext2, font, fontScale, colortext, thicknesstext, cv2.LINE_AA)


            #prints whether inside circle or not
            if radiuscenter > radius2 + d:
                print("inside circle")
                text3comment = "inside the circle"
                text3 = cv2.putText(frames[i], text3comment, coordinatestext3, font, fontScale, colortext, thicknesstext, cv2.LINE_AA)
                
            elif radiuscenter<radius2 + d:
                print("its outside the circle and ")
                

                if mouthwidth > windwidth:
                    print("its at the right")
                    text4comment = "its outside and at the right"
                    text4 = cv2.putText(frames[i], text4comment, coordinatestext3, font, fontScale, colortext, thicknesstext, cv2.LINE_AA) 
                

                elif mouthwidth < windwidth:
                    print("its at the left")
                    text5comment = "its outside and at the left"
                    text5 = cv2.putText(frames[i], text5comment, coordinatestext3, font, fontScale, colortext, thicknesstext, cv2.LINE_AA)

                else:
                    break
                
            #preparing  videooutput with the necessary frame size and writing it
            vidout = cv2.resize(frames[i],(300,300))
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

