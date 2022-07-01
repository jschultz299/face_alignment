import face_alignment
import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt


#Reads image in color 
input_img = cv2.imread('shark.png')

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', face_detector='sfd') # 'cpu' for cpu, 'cuda' for gpu

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


# Get facial landmarks
if input_img is not None:
    det = fa.get_landmarks(input_img)

# Show points
if det is not None:
    Points = det[-1].astype(int)
    mouth_points = Points[48:60, :] # coordinates of the mouth, both columns and elements 48-60
    mouth_center = np.mean(mouth_points) #averages the mouth points numpy array

    #actually puts the points on the face 
    frame = show_points(mouth_points, input_img)


    #prints out elemetns of mouth points to check 
    print(Points[48:60,:])
    # a = mouth_points[1,:]
    # print(a)

    #Making the for loop to average all the points of the mouth to get to the center 
    i = 0
    a = 0
    b = 0
 
    for i in range(0,12): 
        a = a + mouth_points[i,0]
        b = b + mouth_points[i,1]
        avga = a/12
        avgb = b/12
        # print("b: ")
        # print(b)

# checking if it gets the correct averages 
avga =round(avga)
avgb = round(avgb)
print("this is avg b: ")
print(avgb)

cv2.circle(input_img, (avga,avgb), radius, color2, thickness)
        
        

plt.imshow(input_img)


    

# Display the resulting frame
cv2.imshow('frame2', input_img)
cv2.waitKey(0)

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