# 이진화
# 이미지의 픽셀 값을 0과 1(0과 255) 두 가지 값만 가지도록 만드는 영사 처리 기법
# OCR, 윤곽 검출, 객체 분할, 문서 스캔 등 작업에 유리

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/cells.png', cv2.IMREAD_GRAYSCALE)
# 히스토그램 계산(이미지의 픽셀 값 분포를 나타냄)
# calcHist(히스토그램을 계산할 이미지 목록, 그레이스케일 이미지의 채널, 마스크를 사용하지 않음, 빈(bin)을 사용하여 0부터 255까지의 픽셀 값 분포를 계산, 0 ~ 255의 픽셀 값의 범위)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

# 임계값을 기준으로 이미지를 이진화
# threshold(이진화를 적용할 이미지, 임계값, 임계값을 넘는 픽셀에 부여할 최대값, 임계값 적용방식)
# THRESH_BINARY: 픽셀 값이 임계값보다 크면 최대값으로 설정, 작거나 같으면 0으로 설정
# a, dst1: a(임계값), dst1(이진화가 적용된 이미지)
a, dst1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
print(a)
b, dst2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
print(b)
c, dst3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(c)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

plt.plot(hist)
plt.show()
cv2.waitKey()