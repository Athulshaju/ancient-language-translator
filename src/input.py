# # import cv2 as cv
# # import numpy as np
# # capture=cv.VideoCapture(1)
# # def takeInput(event):
# #     if event==cv.EVENT_LBUTTONDOWN:
# #         cv.imread(rectangle)
# # while True:
# #     isTrue,frame=capture.read()
# #     rectangle=cv.rectangle(frame,(300,150),(500,300),(0,255,0),thickness=2)
# #     cv.imshow("video",frame)
    
# #     if cv.waitKey(20) & 0xFF==ord("d"):
# #         break
# # capture.release()
# # cv.destroyAllWindows()

# import cv2
# import numpy as np

# # Open a video capture (change the argument to the video file path if needed)
# cap = cv2.VideoCapture(0)

# while True:
#     # Read a frame from the video capture
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Get the frame dimensions
#     height, width, _ = frame.shape

#     # Define rectangle parameters
#     rect_width = 400
#     rect_height = 200

#     # Calculate the coordinates for the top-left corner of the rectangle to center it
#     center_x = (width - rect_width) // 2
#     center_y = (height - rect_height) // 2

#     # Draw the rectangle on the frame
#     rectangle = cv2.rectangle(frame, (center_x, center_y), (center_x + rect_width, center_y + rect_height), (255, 0, 0), 2)

#     # Display the frame with the centered rectangle
#     cv2.imshow('Centered Rectangle', frame)

#     # Break the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('d'):
#         break

# # Release the video capture and close the OpenCV window
# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np


cap = cv2.VideoCapture(0)


rect_width = 400
rect_height = 400


rect_x, rect_y = 0, 0


def on_mouse_click(event, x, y, flags, param):
    global rect_x, rect_y
    if event == cv2.EVENT_LBUTTONDOWN:
        rect_x = x - rect_width // 2
        rect_y = y - rect_height // 2


cv2.namedWindow('Video Capture')
cv2.setMouseCallback('Video Capture', on_mouse_click)

while True:
    
    ret, frame = cap.read()

   
    rectangle = cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (255, 0, 0), 2)

   
    cv2.imshow('Video Capture', rectangle)

    
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break


cap.release()
cv2.destroyAllWindows()
