import cv2

# ROI(Region of Interest): 관심 영역
img = cv2.imread('./images/sun.jpg')

x = 155
y = 19
w = 102
h = 92

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()
img[y:y+h, x+w:x+w+w] = roi

# 두 태양을 박스로 감싸기
cv2.rectangle(img, (x, y), (x+w+w, y+h), 2)

cv2.imshow('img', img)
cv2.waitKey()