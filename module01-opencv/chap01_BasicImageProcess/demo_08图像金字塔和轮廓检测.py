# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 12:27
import cv2

img = cv2.imread("D://python//opencv_python_project//chap_00data//AM.png")
print(img.shape)

# 高斯金字塔

img_up = cv2.pyrUp(img)
print(img_up.shape)
cv2.imshow("img_up", img_up)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_down = cv2.pyrDown(img)
print(img_down.shape)
cv2.imshow("img_down", img_down)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_up_down = cv2.pyrDown(cv2.pyrUp(img))
print(img_up_down.shape)
cv2.imshow("img_up_down", img_up_down)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 2 拉普拉斯金字塔

down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down)
lap = img - down_up
cv2.imshow("lap", lap)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# 3 轮廓检测
car_img = cv2.imread("D://python//opencv_python_project//chap_00data//contours.png")
gray_car = cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_car, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
cv2.waitKey(1000)
cv2.destroyAllWindows()

binary, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
draw = car_img.copy()
res = cv2.drawContours(draw, contours, -1, (0, 0, 255), 2)
cv2.imshow("res", res)
cv2.waitKey(1000)
cv2.destroyAllWindows()