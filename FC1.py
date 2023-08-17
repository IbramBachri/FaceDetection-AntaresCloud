import cv2
import threading
import time

from antares_http import antares
b=0

model = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(model)
cap = cv2.VideoCapture(0)

def task():
    while True:
          antares.setDebug(True)
          antares.setAccessKey('YOUR ACCESS KEY')
          myData = {
               'count' : b
               }

          antares.send(myData, 'YOUR APLICATIONS', 'YOUR DEVICE')
          time.sleep(15)  # Menunda eksekusi selama 10 detik
          
if _name_ == '_main_':
    # Membuat objek Thread untuk tugas
    thread = threading.Thread(target=task)

    # Memulai eksekusi dari thread
    thread.start()

while True:
     ret, frame = cap.read()
     flipped = cv2.flip(frame, flipCode = -1)
     frame1 = cv2.resize(flipped, (640, 480))
     gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
     b = 0
     
     for (x, y, w, h) in faces:
         x1,y1 = y+w, y+h
         cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
         b=len(faces)
         cv2.putText(frame1,"Count : "+str(b),(20,50),0,2,(255,0,0),3)
         
     cv2.imshow('Deteksi Wajah', frame1)
     
     if cv2.waitKey(1) == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()