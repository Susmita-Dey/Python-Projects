import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image.png')

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)

# display image after detection
cv2.imshow('img', img)
# wait for a few seconds
cv2.waitKey()

# create a new image having rectangle to showcase the detected face
cv2.imwrite("face_detected.png", img)
