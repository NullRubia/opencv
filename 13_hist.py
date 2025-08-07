import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)
# 히스토그램
# 이미지 히스토그램: 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인진 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# 히스토그램 계산(이미지의 픽셀 값 분포를 나타냄)
# calcHist(히스토그램을 계산할 이미지 목록, 그레이스케일 이미지의 채널, 마스크를 사용하지 않음, 빈(bin)을 사용하여 0부터 255까지의 픽셀 값 분포를 계산, 0 ~ 255의 픽셀 값의 범위)
# images: 대상 이미지 리스트
# channel: 분석할 채널 번호(b:0, g:1, r:2)
# mask: 분석할 영역 마스크(None: 전체)
# histSize: 히스토그램의 빈 개수
# ranges: 값의 범위
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist1, color='gray')
img2 = cv2.imread('./images/candies.png')
print('shape: ', img2.shape)
print('dtype: ', img2.dtype)
'''
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
'''
colors = ['b', 'g', 'r']
channels = cv2.split(img2)
plt.subplot(1, 2, 2)
for ch, color in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 255])
    plt.plot(hist, color=color, label=color.upper())
b, g, r = cv2.split(img2)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
plt.plot(hist1)
plt.show()
cv2.waitKey()