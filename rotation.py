import cv2

img = cv2.imread("nightshade.png")
cv2.imshow("Ironman", img)
cv2.waitKey(0)

img2 = cv2.imread("ironman.png")

hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
cv2.imshow("Gray Ironman", hsv)
cv2.waitKey(0)

grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Ironman", grayimage)
cv2.waitKey(0)

# manual grayscale
print(img.shape)
row, column = img.shape[0:2]
for i in range(row):
    for j in range(column):
        img[i,j] = sum(img[i,j]) // 3
cv2.imshow("Gray Manual", img)
cv2.waitKey(0)

edges = cv2.Canny(img2, 100, 200)
cv2.imshow("Edges", edges)
cv2.imwrite("edges.png", edges)

        
        