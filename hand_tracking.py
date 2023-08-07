import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mpHands = mp.solution.hands   
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.Color(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    cv2.imshow("Image", img)
    cv2.WaitKey(1)
    