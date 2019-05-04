import cv2 as cv
import numpy as np

mask=np.zeros([1080,1920],dtype=np.uint8)

for w in range(0,1920):
    for h in range(0,1080):
        if not ((h<(-910/800)*w+910+100)or(h<(910/800)*w-1274+100)or((h>(-1080/260)*w+4000)and(h>(1080/260)*w-4000))):
            mask[h,w]=255

cv.imwrite("./MASK.jpg",mask)       #全景遮罩
image = cv.imread('C:/Users/yjy84/Desktop/1.jpg')       #读取原片
image = cv.add(image, np.zeros(np.shape(image), dtype=np.uint8), mask=mask)     #对原片进行全景遮罩
cv.imwrite("./RIO.jpg",image)       #全景遮罩原片输出
image=image[360:720,:]
cv.imwrite("./REAL-RIO.jpg",image)

mask=mask[360:720,:]
mask = cv.resize(mask, (384,80), interpolation=cv.INTER_AREA)
cv.imwrite("C:/Users/yjy84/Desktop/MASK.png",mask)

# sss[0:200,0:600]=255
#
# cv.imwrite("./1.png",sss)
# src=cv.imread("./1.png")
# cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
# cv.imshow('input_image', src)
input("请按任意键继续")
# print(mask)
