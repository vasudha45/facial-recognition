import cv2
import os
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('pic2.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.05,4)

directory = os.getcwd()+r''

try:
    os.mkdir(directory)
except FileExistsError as fee:
    print('Exception Occured',fee)
os.chdir(directory)
i=1
for (x, y, w, h) in faces:
    FaceImg = img[y:y+h,x:x+w]
    # To save an image on disk
    filename = 'Face'+str(i)+'.jpg'
    cv2.imwrite(filename,FaceImg)
    i+=1

num = 1
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    org = (x-10,y-10)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (255, 0, 0)
    thickness = 2

    i = cv2.putText(img, str(num), org, font,
               fontScale, color, thickness, cv2.LINE_AA)
    num = num+1

cv2.imshow('img', img)
cv2.waitKey()