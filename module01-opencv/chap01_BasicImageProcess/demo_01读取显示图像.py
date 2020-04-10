# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 9:24
import cv2

print(cv2.__version__)
# 1 彩色图像
img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg")  # BGR
print(img.shape)
print(img.size)
print(img.dtype)
print(type(img))
cv2.imshow("image", img)
cv2.waitKey(100)  # 等待时间，0表示自己控制显示终止
cv2.destroyAllWindows()

# 2 灰度图像
img_gray = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray", img_gray)
cv2.waitKey(10)
cv2.destroyAllWindows()

# 3 保存图像
img_write = cv2.imwrite("D://python//opencv_python_project//chap_00data//img_write.png", img)
print(img_write)

