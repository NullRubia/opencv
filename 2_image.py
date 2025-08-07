import cv2

# 그레이스케일 영상
img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
print(img1)

print("-----------------------------")
# 트루컬러 영상
img2 = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR 생략 가능
print(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey() #특정키를 누를때 까지 종료 막기