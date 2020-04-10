# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 12:10
"""
1 高斯滤波器，平滑图像，去除噪声
2 计算每个像素中的梯度大小和梯度方向sobel
3 非极大值抑制，消除边缘检测带来的杂散响应，线性差值
4 使用双阈值检测来确定真实的和潜在的边缘
5 通过抑制边缘孤立的弱化边缘完成检测
"""
import cv2
import numpy as np

lena_gray_img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(lena_gray_img, 80, 150)
v2 = cv2.Canny(lena_gray_img, 50, 100)

v = np.hstack((v1, v2))
cv2.imshow("lena_xy", v)
cv2.waitKey(1000)
cv2.destroyAllWindows()

car_gray_img = cv2.imread("D://python//opencv_python_project//chap_00data//car.png", cv2.IMREAD_GRAYSCALE)

car_v1 = cv2.Canny(car_gray_img, 120, 250)
car_v2 = cv2.Canny(car_gray_img, 50, 100)

car_v = np.hstack((car_v1, car_v2))
cv2.imshow("lena_xy", car_v)
cv2.waitKey(0)
cv2.destroyAllWindows()