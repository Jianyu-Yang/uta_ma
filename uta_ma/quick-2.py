import cv2 as cv
import numpy as np
import time
import datetime
# from PIL import Image


def detect_circles_demo(image):
    time_start = time.time()
    image=image[165:285,:]      #截取ROI
    # image = cv.pyrDown(image)     #高斯金字塔
    # image = image.resize((75,35),Image.ANTIALIAS)      #抗锯齿
    image = cv.resize(image, (300,60), interpolation=cv.INTER_AREA)     #压缩图像
    #cv.imshow("ROI", image)
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)   #边缘保留滤波EPF
    #cv.imshow("EPF", dst)
    cimage = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    #cv.imshow("GRAY", cimage)
    #canny=cv.Canny(cimage, 40, 80)
    #cv.imshow("Canny", canny)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=80, param2=9, minRadius=10, maxRadius=15)
    
    # circles = np.uint16(np.around(circles)) #把circles包含的圆心和半径的值变成整数
    # print(circles.size/3)
    if len(circles[0])!=0:
        #ww=1
        for i in circles[0, : ]:
            cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  #画圆
            cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)  #画圆心
    else:
        cv.imshow("no-circles", image)
        end=time.clock()
        print('未检测到圆-程序运行时间：', datetime.timedelta(seconds=time.time() - time_start))
        return
    cv.imshow("circles", image)
    print('程序运行时间：', datetime.timedelta(seconds=time.time() - time_start))

src = cv.imread('C:/Users/Administrator/Desktop/1.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
input("请按任意键继续")
