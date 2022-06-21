import face_alignment
import cv2
import numpy as np
import torch
import matplotlib.pyplot as plt

from skimage import io


cap = cv2.VideoCapture(14)
# input_img = io.imread('twofaces.jpg')
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', face_detector='sfd')
frames = []

while(True):
      
    # Capture the video frame
    # by frame
    success, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)

    det = fa.get_landmarks_from_image(frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
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