import cv2 as cv
import numpy as np

# img = cv.imread("img_1.jpg")
# cv.imshow("window", img)
# cv.waitKey(0)

# img = cv.imread("img_1.jpg")
# cv.imshow("window", img)
# cv.waitKey(0)

# to play video 

# capture = cv.VideoCapture("video_2_Sydney.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)
    
#     if cv.waitKey(50) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# Resizing and Rescaling

# def rescaleFrame(frame , scale = 0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
    
#     dimensions = (width , height)
    
#     return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)


# capture = cv.VideoCapture("video_2_Sydney.mp4")

# while True:
#     isTrue, frame = capture.read()
    
#     frame_resized = rescaleFrame(frame)
    
#     cv.imshow("Video", frame)
#     cv.imshow("Video Resized" , frame_resized)
    
#     if cv.waitKey(10) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

#resized images

# img = cv.imread("img_2.png")
# resized_image = rescaleFrame(img)
# cv.imshow("Resized img", resized_image)
# cv.imshow("orignal", img)

# cv.waitKey(0)

# img3 = cv.imread("dog/dog1.jpg")
# cv.imshow("dog", img3)
# cv.waitKey(0)

#To make blank image

# blank = np.zeros((500,500,3) , dtype = 'uint8')
#cv.imshow('Blank', blank)
# cv.waitKey(0)

# #1 - paint the image with certain color
# blank[:] = 255,255,255
# cv.imshow('Green', blank)
# cv.waitKey(0)

# blank[:] = 0,0, 255
# cv.imshow('Red', blank)
# cv.waitKey(0)

# blank[100:200 , 200:400] = 0,255,0
# cv.imshow('Red_Green', blank)
# cv.waitKey(0)

# To draw rectangle

blank = np.zeros((500,500, 3) , dtype = 'uint8')
# cv.rectangle(blank, (250,250), (500,500), (0,255,0) , thickness =2)

# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

#to draw circle 

# cv.circle(blank, (250,250) , 100 , (0,0,255), thickness = -2)
# cv.imshow('circle', blank)
# cv.waitKey(0)

# cv.line(blank, (:,250), (:,250), (0,0, 255), thickness= 2)
# cv.imshow('line', blank)
# cv.waitKey(0)

# to put text on image


# cv.putText(blank,"Hello from icode",(100,255), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), 2 )
# cv.imshow('text', blank)
# cv.waitKey(0)