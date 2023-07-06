import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)


mpHands =mp.solutions.hands
hands = mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils

pTime= 0
cTime = 0

while True:
    success , img= cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if  results.multi_hand_landmarks:
       for handLms in results.multi_hand_landmarks:
           for id, lm in enumerate(handLms.landmark):
               print(id,lm) # burada elimizi tararırken olusşan noktarın konumunu ve idlerini ekrana yazdırıyor
               h,w,c = img.shape
               cx,cy = int(lm.x*w) , int(lm.y*h) # burada decimal olan kordinatları  int çeviriyor

               print( id ,cx,cy) # burada bize 0 ile 20 arasında numaralı olan noktarın id lerini ve kordinatalrını gösteriyor
               mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
               if id ==  4:
                cv2.circle(img, (cx ,cy),15,(255,0,255),cv2.FILLED) # BURRADA İD Sİ 0 OLAN NOKTANIN ETRAFINI daire ile çizmesini söyledik

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)

    cv2.imshow('İmage',img)
    cv2.waitKey(1)