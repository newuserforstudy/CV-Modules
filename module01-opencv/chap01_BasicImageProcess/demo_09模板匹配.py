# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 13:04
import cv2

img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", 0)
print(img.shape)
face = img[90:200, 110:185]
cv2.imshow("face", face)
cv2.waitKey(1000)
cv2.destroyAllWindows()

res = cv2.matchTemplate(img, face, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_loc, max_loc)
img2 = img.copy()
t = cv2.rectangle(img2, min_loc, max_loc, 255, 3)
cv2.imshow("t", t)
cv2.waitKey(1000)
cv2.destroyAllWindows()
