import cv2 #library Import OpenCV

img = cv2.imread("logo.png") #read Image
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #COLOR TO GRAY IMAGE
cv2.imwrite("grayImg.png",img) #save Image

cv2.imshow("Gray",grayImg)
cv2.imshow("orig",img) 
cv2.waitKey(0)

cv2.destroyAllWindows()

