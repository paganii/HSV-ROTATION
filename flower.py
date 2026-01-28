import cv2
import os

img = cv2.imread("nightshade.png", cv2.IMREAD_COLOR)
cv2.imshow("Colored Flower", img)

path = "C:/Users/Hp/OneDrive/Desktop"
img2 = cv2.imread("nightshade.png", 0) # 0 is grayscale
cv2.imshow("NS as BNW", img2)
cv2.waitKey(0)
cv2.imwrite("NightshadeBW.png", img2) #saving
img3 = cv2.imread("NightshadeBW.png", 0)
cv2.imshow("Nightshade latest", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()