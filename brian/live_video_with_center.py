import face_alignment
import cv2
import numpy as np
import torch
from skimage import io
import matplotlib.pyplot as plt


#inputing video
cap = cv2.VideoCapture(0)

# Sets up the facial recognition package 
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', face_detector='sfd') # 'cpu' for cpu, 'cuda' for gpu
frames = []

# adjusting size and color of points on the face 
radius = 3
color = (100, 200, 200)
color2 = (200, 0, 0)
thickness = -1

#function that shows points on face 
def show_points(Points, frame):
    for point in Points:
        frame = cv2.circle(frame, tuple(point), radius, color, thickness)

    return frame

while(True):
    # Capture the video frame
    # by frame
    success, frame = cap.read()
    # Get facial landmarks
    if frame is not None:
        det = fa.get_landmarks(frame)

    # Selecting the points surrounding the mouth 
        if det is not None:
            Points = det[-1].astype(int)
            mouth_points = Points[48:60, :] # coordinates of the mouth, both columns and elements 48-60
            frame = show_points(mouth_points, frame)#actually puts the points on the face 

    #Defining the variables for the loop
            i = 0
            a = 0
            b = 0
    #For loop of 12 because there are 12 rows in the mouth points and averaging these points to get center
            for i in range(0,12): 
                a = a + mouth_points[i,0]
                b = b + mouth_points[i,1]
                avga = a/12
                avgb = b/12 
                print("A is : ")
                print(avga)

    #Displaying the center of the mouth as well and the markers surrounding the mouth 
            cv2.circle(frame, (int(avga),int(avgb)), radius, color2, thickness)

            cv2.imshow('frame', frame)

        
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Display the resulting frame

cap.release()
cv2.destroyAllWindows()

# success, frame = cap.read()
# cv2.imshow('frame', frame)
# # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
# det = fa.get_landmarks_from_image(frame)

# print(det)
# plt.imshow(frame)
# plt.show()

# if det is not None:
#     for detection in det:
#         plt.scatter(detection[:,0], detection[:,1], 2)

# plt.show()


# while True:
#     success, frame = cap.read()
#     if not success:
#         break
    
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # frames.append(frame)
    
#     det = fa.get_landmarks_from_image(frame)
#     print(type(det))

#     plt.imshow(frame)
#     if det is not None:
#         for detection in det:
#             plt.scatter(detection[:,0], detection[:,1], 2)