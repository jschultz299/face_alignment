import face_alignment
from skimage import io
#import collections
from skimage.measure import EllipseModel
import sys
import numpy as np
import cv2

def mouthOpen(Points):
    mouth_points = Points[48:60]
    # X = mouth_points[:,0]
    # Y = mouth_points[:,1]
    # X.shape = (12,1)
    # Y.shape = (12,1)

    ell = EllipseModel()
    ell.estimate(mouth_points)

    xc, yc, a, b, theta = ell.params

    temp = [a, b]
    a = max(temp)
    b = min(temp)

    ratio = a / b

    # print("center = ",  (xc, yc))
    # print("angle of rotation = ",  theta)
    # print("axes = ", (a,b))
    # print(("Ratio = ", ratio))

    # print(("\n-------------------\n"))

    if ratio > .5 and ratio < 2.0:
        mouth_open = True
    else:
        mouth_open = False

    return mouth_open, xc, yc, theta, a, b


def main():
    # Optionally set detector and some additional detector parameters
    face_detector = 'sfd'
    face_detector_kwargs = {
        "filter_threshold" : 0.8
    }

    # Run the 3D face alignment on a test image, without CUDA.
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', flip_input=True,
                                      face_detector=face_detector, face_detector_kwargs=face_detector_kwargs)

    # Get input image
    try:
        input_img = io.imread('face.jpg')
    except FileNotFoundError:
        input_img = io.imread('face.jpg')

    # Get detections
    det = fa.get_landmarks(input_img)[-1]
    
    frame = input_img

    radius = 3
    thickness = -1

    xc_list = list()
    yc_list = list()
    theta_list = list()
    a_list = list()
    b_list = list()

    Points = det.astype(int)

    mouth_open, xc, yc, theta, a, b = mouthOpen(Points)

    xc_list.append(xc)
    yc_list.append(yc)
    theta_list.append(theta)
    a_list.append(a)
    b_list.append(b)
#    if image_counter > movingAverageWindow:
#        xc_list.pop(0)
#        yc_list.pop(0)
#        theta_list.pop(0)
#        a_list.pop(0)
#        b_list.pop(0)

    mean_xc = np.mean(xc_list)
    mean_yc = np.mean(yc_list)
    mean_theta = np.mean(theta_list)
    mean_a = np.mean(a_list)
    mean_b = np.mean(b_list)

    if mouth_open:
        mouth_color = (0, 255, 0)
    else:
        mouth_color = (0, 0, 255)

    for i in range(60):
        point = Points[i]

        if i > 47:
            # Mouth Color
            color = mouth_color
            radius = 3
        else:
            color = (255, 0, 0)
            radius = 2
            
    frame = cv2.ellipse(frame, (int(round(mean_xc)), int(round(mean_yc))), (int(round(mean_a)), int(round(mean_b))), int(round(mean_theta)), 0., 360, color)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    cv2.waitKey(0)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
#    # After the loop release the cap object
#    cap.release()
#    # Destroy all the windows
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
