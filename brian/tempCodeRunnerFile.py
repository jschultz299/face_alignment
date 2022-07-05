for i in range(0,20):
#     if frames[i] is not None:
#         det = fa.get_landmarks(frames[i])

#         if det is not None:
#             Points = det[-1].astype(int)
#             mouth_points = Points[48:60, :] # coordinates of the mouth, both columns and elements 48-60
#             frames[i] = show_points(mouth_points, frames[i])#actually puts the points on the face 

#             # Defining the variables for the loop
#             cv2.circle(frames[i], (int(avga(0,0,0)),int(avgb(0,0,0))), radius, color2, thickness)

            

            
#             # img = cv2.imwrite('test'+str(i)+'.jpg',frames[i]) # equal it to something 

#             # print(img)
#             vidout=cv2.resize(frames[i],(300,300))
#             video.write(vidout)
#             cv2.imshow('frame',frames[i])

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break        
#         # i = 0
#         # a = 0
#         # b = 0
#     #For loop of 12 because there are 12 rows in the mouth points and averaging these points to get center
#         # for i in range(0,12): 
#         #     a = a + mouth_points[i,0]
#         #     b = b + mouth_points[i,1]
#         #     avga = a/12
#         #     avgb = b/12 
#         #     # print("A is : ")
#             # print(avga)

#     # Displaying the center of the mouth as well and the markers surrounding the mouth 

# video.release()    
# cap.release()
# cv2.destroyAllWindows()
