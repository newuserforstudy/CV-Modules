# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 11:12
import cv2
import numpy as np

img = cv2.imread("D://python//opencv_python_project//chap_00data//dige.png")
cv2.imshow("img", img)
cv2.waitKey(100)
cv2.destroyAllWindows()

# 1 腐蚀操作
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("ierosion ", erosion)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 2 膨胀操作
img_dilate = cv2.dilate(erosion, kernel, iterations=1)
cv2.imshow("img_dilate  ", img_dilate)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 3 开运算和闭运算
# 开运算:先腐蚀，再膨胀
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("open_img", open_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 闭运算：先膨胀，再腐蚀
close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("open_img", close_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 4 梯度运算
gradient_img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gradient_img", gradient_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 5 礼帽和黑帽
# 礼帽：原始输入-开运算
top_hat_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("top_hat_img", top_hat_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 黑帽：闭运算-原始输入
black_hat_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("top_hat_img", top_hat_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
