import cv2

img = cv2.imread('assets/first.png',1)
'''
-1.trasparency
0.grayscale
1 unchanged
'''

img = cv2.resize(img,(0,0),fx=0.75 ,fy=0.75)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg',img)

cv2.imshow('Image', img)
cv2.waitKey(0)  # 0 = unless u press key
cv2.destroyAllWindows()