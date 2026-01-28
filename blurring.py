import cv2
import os

image = cv2.imread("bridge.png", cv2.IMREAD_UNCHANGED) #_COLOR; _GRAYSCALE; _UNCHANGED
mblurring = cv2.medianBlur(image, 5)
mblurred = cv2.imwrite("MBlurred.png", mblurring)
cv2.imshow("MedianBlurred Result", mblurring)
cv2.waitKey(0)


bilatering = cv2.bilateralFilter(image, 9, 75, 75)
bilaterated = cv2.imwrite("bilateratedPng.png", bilatering)
cv2.imshow("Bilaterated Result", bilatering)
cv2.waitKey(0)

borderingImg = cv2.copyMakeBorder(image, 10, 15, 10, 15, cv2.BORDER_CONSTANT, value = (1))
borderedsave = cv2.imwrite("bordered.png", borderingImg)
cv2.imshow("Bordered Result", borderingImg)
cv2.waitKey(0)
