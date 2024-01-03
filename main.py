'''
Name: Abu Bakar
Md. Didarul Alam
Id: 190311002
uctc

'''

import cv2
import numpy as np 
import time 
import os
import handTrackModule as htm # hand tracking module

folderPath = "Header"
myList = os.listdir(folderPath)


# ###########################
brushThickness =15
eraserThickness = 100
# ##########################
overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(image)

header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((480, 640, 3), np.uint8)

while True:
    # step 1: image import
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # step 2: find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # fingers selection
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # step 3: check which fingers are up
        fingers = detector.fingersUp()

        # step 4: If selection mode two fingers are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0

            # checking for the click
            if y1 < 63:
                if 133 < x1 < 165:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 215 < x1 < 247:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 379 < x1 < 415:
                    header = overlayList[2]
                    drawColor = (255, 255, 0)
                elif 465 < x1 < 497:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1-28), (x2,y2+28), drawColor,cv2.FILLED)

        # step 5: If drawing mode - index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            

            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    
    # setting the header image
    img[0:63,0:640, 0:3] = header
    img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("Input Canvas", img)
    cv2.imshow("Output Canvas", imgCanvas)
    cv2.imshow("Inv Canvas", imgInv)
    cv2.waitKey(1)