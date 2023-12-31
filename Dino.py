import cv2
import math
import numpy as np
import pyautogui
import time
from cvzone.HandTrackingModule import HandDetector
import webbrowser


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)
detector = HandDetector(detectionCon=0.8, maxHands=1)

#cv2.namedWindow('Dino Game', cv2.WINDOW_NORMAL)
time.sleep(3)
pyautogui.keyDown(key='win')            
pyautogui.press('right') 
pyautogui.keyUp(key='win')  

webbrowser.open("https://offline-dino-game.firebaseapp.com/")
time.sleep(3)

pyautogui.keyDown(key='win')            
pyautogui.press('left') 
pyautogui.keyUp(key='win') 

while True:
    success, img = cap.read()
    hands,img=detector.findHands(img)
    if hands:
        hand1=hands[0]
        lmList1=hand1["lmList"]
        
        x1,y1,_=lmList1[4]
        x2,y2,_=lmList1[8]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        if length<25:
            cv2.circle(img, (cx, cy), 10, (0,255, 0), cv2.FILLED)
        #print(length)
        vol = np.interp(length, [40, 50], [0, 1])
        print(int(vol))
        if vol==1:
            pyautogui.press("space")
    cv2.imshow("image",img)
    cv2.waitKey(1)   