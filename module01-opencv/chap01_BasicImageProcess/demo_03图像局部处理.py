# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 9:57
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg")

print(img.shape)
obj = img[10:200, 10:200, :]

cv2.imshow("obj", obj)
cv2.waitKey(1000)
cv2.destroyAllWindows()

b, g, r = cv2.split(img)
print(b.shape)
print(g.shape)
print(r.shape)

img_copy = img.copy()
img_copy[:, :, 0] = 0
img_copy[:, :, 1] = 0

cv2.imshow("copy", img_copy)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 填充
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
# 赋值法
replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
# 反射法:在两边复制 ba|abcd|dcb
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
# 发射法:以最边缘为轴 cb|abcd|cba
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
# 外包装法
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# 常量法
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=0)

plt.subplot(231), plt.imshow(img, "gray"), plt.title("ORIGION")
plt.subplot(232), plt.imshow(replicate, "gray"), plt.title("replicate")
plt.subplot(233), plt.imshow(reflect, "gray"), plt.title("reflect")
plt.subplot(234), plt.imshow(reflect101, "gray"), plt.title("reflect101")
plt.subplot(235), plt.imshow(wrap, "gray"), plt.title("wrap")
plt.subplot(236), plt.imshow(constant, "gray"), plt.title("constant")
plt.show()
