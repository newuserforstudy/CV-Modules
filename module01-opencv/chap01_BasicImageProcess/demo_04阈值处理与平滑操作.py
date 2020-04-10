# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 10:50
import cv2
import matplotlib.pyplot as plt

# 图像阈值
img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["origion", "THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray"), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# 平滑处理
img_noise = cv2.imread("D://python//opencv_python_project//chap_00data//lenaNoise.png")
cv2.imshow("noise", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 均值滤波
blur = cv2.blur(img_noise, (3, 3))
cv2.imshow("blur", blur)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 方框滤波
box = cv2.boxFilter(img_noise, -1, (3, 3), normalize=True)
cv2.imshow("box", box)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# 高斯滤波
gauss = cv2.GaussianBlur(img_noise, (5, 5), 1)
cv2.imshow("gauss", gauss)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 中值滤波
medium = cv2.medianBlur(img_noise, 5)
cv2.imshow("medium", medium)
cv2.waitKey(1000)
cv2.destroyAllWindows()
