# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 16:46
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1 直方图
img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", 0)
hist_cal = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist_cal)
plt.hist(img.ravel(), 256)
plt.show()

img_cat = cv2.imread("D://python//opencv_python_project//chap_00data//cat.jpg")
color = ("b", "g", "r")
for i, col in enumerate(color):
    hist_c = cv2.calcHist([img_cat], [i], None, [256], [0, 255])
    plt.plot(hist_c, color=col)
    plt.xlim([0, 256])
plt.show()

# 2 掩码
mask = np.zeros(img_cat.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
cv2.imshow("mask", mask)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_cat_gray = cv2.cvtColor(img_cat, cv2.COLOR_BGR2GRAY)
mask_img = cv2.bitwise_and(img_cat_gray, img_cat_gray, mask=mask)
cv2.imshow("mask_img", mask_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

hist_full = cv2.calcHist([img_cat_gray], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([mask_img], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(img_cat_gray, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(mask_img, "gray")
plt.subplot(224), plt.plot(hist_full, "r"), plt.plot(hist_mask, "k")
plt.xlim([0, 256])
plt.ylim([0, 4000])
plt.show()

plt.plot(hist_full, "r"), plt.plot(hist_mask, "k")
plt.xlim([0, 256])
plt.ylim([0, 4000])
plt.show()

# 3 直方图均衡化

img_hist = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", 0)
plt.hist(img_hist.ravel(), 256)
plt.show()

equ_img = cv2.equalizeHist(img_hist)
plt.hist(equ_img.ravel(), 256)
plt.show()

res = np.hstack((img_hist, equ_img))
cv2.imshow("res ", res)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img = cv2.imread("D://python//opencv_python_project//chap_00data//clahe.jpg", 0)
equ = cv2.equalizeHist(img)

# 自适应均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
res_clahe = clahe.apply(img)

res = np.hstack((img, equ, res_clahe))
cv2.imshow("res ", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
