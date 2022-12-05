import cv2
tdata=cv2.CascadeClassifier('face.xml')
img=cv2.imread('aliya.jfif')
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fcoordinates=tdata.detectMultiScale(gimg)
x,y,w,l=fcoordinates[0]
cv2.rectangle(img,(x,y),(x+w,y+l),(0,0,255),2)
cv2.imshow('aliya',img)
cv2.waitKey()
print('EOP')