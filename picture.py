import cv2
import random
img = cv2.imread("assets/first.png",1)

print(img.shape) 
'''
blue green red
 print(img[554][200]) - to get the exact pixel value [rows][pixel]

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] =[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
'''

tag = img[200:250,600:800]
img[150:200,300:500] =tag



cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows