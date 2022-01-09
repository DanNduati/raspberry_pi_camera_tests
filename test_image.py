import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cv2.imwrite(f'images/image_{datetime.now()}.jpg', frame)
cap.release()
