# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2020/4/7 0007 17:34

"""
高频：变换剧烈的部分
低频：变换缓慢的部分

低通滤波：保存低频，图像变模糊
高通滤波：保存高频，图像细节增强
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D://python//opencv_python_project//chap_00data//lena.jpg", 0)
img = np.float32(img)
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
# 灰度图表示形式
mag = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(mag, cmap="gray"), plt.title("mag image"), plt.xticks([]), plt.yticks([])
plt.show()

row, col = img.shape
c_row, c_col = int(row / 2), int(col / 2)
# 低通滤波器
mask = np.zeros((row, col, 2), np.uint8)
mask[c_row - 30:c_row + 30, c_col - 30:c_col + 30] = 1

fshitf = dft_shift * mask
f_ishift = np.fft.ifftshift(fshitf)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap="gray"), plt.title("img_back"), plt.xticks([]), plt.yticks([])
plt.show()

# 高通滤波器
mask = np.ones((row, col, 2), np.uint8)
mask[c_row - 30:c_row + 30, c_col - 30:c_col + 30] = 1

fshitf = dft_shift * mask
f_ishift = np.fft.ifftshift(fshitf)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("input image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap="gray"), plt.title("img_back"), plt.xticks([]), plt.yticks([])
plt.show()
