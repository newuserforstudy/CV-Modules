# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 11:37
import cv2
import numpy as np

img = cv2.imread("D://python//opencv_python_project//chap_00data//pie.png")
cv2.imshow("img", img)
cv2.waitKey(100)
cv2.destroyAllWindows()

# 1 sobel算子
sobel_img_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
cv2.imshow("sobel_img", sobel_img_x)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_img_x_abs = cv2.convertScaleAbs(sobel_img_x)
cv2.imshow("sobel_img_abs", sobel_img_x_abs)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_img_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
cv2.imshow("sobel_img", sobel_img_y)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_img_y_abs = cv2.convertScaleAbs(sobel_img_y)
cv2.imshow("sobel_img_abs", sobel_img_y_abs)
cv2.waitKey(1000)
cv2.destroyAllWindows()

sobel_img_edge = cv2.addWeighted(sobel_img_x_abs, 0.5, sobel_img_y_abs, 0.5, 0)
cv2.imshow("sobel_img_edge", sobel_img_edge)
cv2.waitKey(1000)
cv2.destroyAllWindows()

lena_gray_img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", cv2.IMREAD_GRAYSCALE)
lena_x = cv2.Sobel(lena_gray_img, cv2.CV_64F, 1, 0, ksize=3)
lena_x = cv2.convertScaleAbs(lena_x)

lena_y = cv2.Sobel(lena_gray_img, cv2.CV_64F, 0, 1, ksize=3)
lena_y = cv2.convertScaleAbs(lena_y)

lena_xy = cv2.addWeighted(lena_x, 0.5, lena_y, 0.5, 0)
cv2.imshow("lena_xy", lena_xy)
cv2.waitKey(1000)
cv2.destroyAllWindows()

lena_xy_all = cv2.Sobel(lena_gray_img, cv2.CV_64F, 1, 1, ksize=3)
lena_xy_all = cv2.convertScaleAbs(lena_xy_all)
cv2.imshow("lena_xy_all", lena_xy_all)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 2 scharr算子
lena_sch_x = cv2.Scharr(lena_gray_img, cv2.CV_64F, 1, 0)
lena_sch_x = cv2.convertScaleAbs(lena_sch_x)
lena_sch_y = cv2.Scharr(lena_gray_img, cv2.CV_64F, 0, 1)
lena_sch_y = cv2.convertScaleAbs(lena_sch_y)

lena_sch_xy = cv2.addWeighted(lena_x, 0.5, lena_sch_y, 0.5, 0)
cv2.imshow("lena_sch_xy", lena_sch_xy)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# 3 laplas
lena_laplacian= cv2.Laplacian(lena_gray_img, cv2.CV_64F)
cv2.imshow("lena_laplacian", lena_laplacian)
cv2.waitKey(1000)
cv2.destroyAllWindows()