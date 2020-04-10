# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 9:45
import cv2

print(cv2.__version__)
video = cv2.VideoCapture("D://python//opencv_python_project//chap_00data/test.mp4")

if video.isOpened():
    op, frame = video.read()
else:
    op = False

while op:
    ret, frame = video.read()
    if frame is None:
        break
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("result", gray)
        if cv2.waitKey(30) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()
