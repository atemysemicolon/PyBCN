import cv2
from skimage import data
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

frame = data.lena();
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imshow('Video', frame)

cv2.waitkey()

# When everything is done, release the capture
video_capture.release()
