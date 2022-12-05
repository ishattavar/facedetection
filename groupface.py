import cv2
from random import randrange as r
tdata=cv2.CascadeClassifier('face.xml')
img=cv2.imread('gp.jpg')
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fcoordinates=tdata.detectMultiScale(gimg)
for x,y,w,l in fcoordinates:

    cv2.rectangle(img,(x,y),(x+w,y+l),(r(0,256),r(0,256),r(0,256)),2)




cv2.imshow('group',img)

cv2.waitKey()
print('EOP')