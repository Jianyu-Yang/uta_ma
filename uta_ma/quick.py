import cv2 as cv
import numpy as np
import time
import datetime
# from PIL import Image

def detect_circles_demo(image):
    time_start = time.time()
    image=image[360:720,:]
    # image = cv.pyrDown(image)     #高斯金字塔
    # image = image.resize((300,65),Image.ANTIALIAS)      #抗锯齿
    image = cv.resize(image, (384,80), interpolation=cv.INTER_AREA)
    image = cv.add(image, np.zeros(np.shape(image), dtype=np.uint8), mask=mask)     #对背景进行遮罩
    # cv.imshow("ROI", image)     # 显示遮罩后的图像
    dst = cv.pyrMeanShiftFiltering(image, 5, 30)   #边缘保留滤波EPF
    cv.imshow("EPF", dst)       #显示滤波后图像
    cimage = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    cv.imshow("GRAY", cimage)       #显示灰度图像
    canny=cv.Canny(cimage, 150, 300)
    cv.imshow("Canny", canny)       #显示Canny边缘检测后图像
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 50, param1=300, param2=18, minRadius=8, maxRadius=19)
    # print(circles)
    if circles is None:
        cv.imshow("circles", image)
        print('未检测到圆-程序运行时间：', datetime.timedelta(seconds=time.time() - time_start))
    else:
        circles = np.uint16(np.around(circles))  # 把circles包含的圆心和半径的值变成整数
        for i in circles[0, :]:
            cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 画圆
            cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)  # 画圆心
        cv.imshow("circles", image)
        print('检测到圆-程序运行时间：', datetime.timedelta(seconds=time.time() - time_start))

cap = cv.VideoCapture("C:/Users/yjy84/Desktop/1.mp4") # 调整参数实现读取视频或调用摄像头
mask=cv.imread("C:/Users/yjy84/Desktop/MASK.png")
mask = cv.cvtColor(mask, cv.COLOR_RGB2GRAY)

# cv.namedWindow('ROI', cv.WINDOW_NORMAL)
cv.namedWindow('EPF', cv.WINDOW_NORMAL)
cv.moveWindow('EPF',100,100)
cv.namedWindow('GRAY', cv.WINDOW_NORMAL)
cv.moveWindow('GRAY',600,800)
cv.namedWindow('Canny', cv.WINDOW_NORMAL)
cv.namedWindow('circles', cv.WINDOW_NORMAL)

while 1:
    ret, frame = cap.read()
    # cv.namedWindow('input_image', cv.WINDOW_NORMAL)  # 设置为WINDOW_NORMAL可以任意缩放
    # cv.imshow('input_image', frame)
    detect_circles_demo(frame)
    if cv.waitKey(50) & 0xff == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()
input("请按任意键继续")
