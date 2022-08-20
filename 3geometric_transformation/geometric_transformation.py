#geometric_transformation.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('light1.jpg')
#图像平移
H = np.float32([[1,0,100],[0,1,50]])
rows,cols = img.shape[:2]
res = cv2.warpAffine(img,H,(rows,cols)) #需要图像、变换矩阵、变换后的大小
plt.subplot(121)
plt.imshow(img,'brg')
plt.subplot(122)
plt.imshow(res,'brg')
#plt.show()
cv2.imwrite("light_warpAffine.jpg", res)
#图像缩放
# 插值：interpolation
# None本应该是放图像大小的位置的，后面设置了缩放比例，
#所有就不要了
res1 = cv2.resize(img,None,fx=8,fy=8,interpolation=cv2.INTER_CUBIC)
#直接规定缩放大小，这个时候就不需要缩放因子
height,width = img.shape[:2]
res2 = cv2.resize(img,(4*width,4*height),interpolation=cv2.INTER_CUBIC)
plt.subplot(131)
plt.imshow(img,'brg')
plt.subplot(132)
plt.imshow(res1,'brg')
plt.subplot(133)
plt.imshow(res2,'brg')
#plt.show()

#图像旋转
rows,cols = img.shape[:2]
#第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
M = cv2.getRotationMatrix2D((cols/3,rows/3),90,1.1)
#第三个参数：变换后的图像大小
res = cv2.warpAffine(img,M,(rows,cols))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
#plt.show()

#图像仿射
rows,cols = img.shape[:2]
pts1 = np.float32([[65,140],[215,150],[55,300]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
#第三个参数：变换后的图像大小
res = cv2.warpAffine(img,M,(rows,cols))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
#plt.show()

#图像透射
rows,cols = img.shape[:2]
pts1 = np.float32([[87,191],[191,198],[78,294],[187,292]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])
M = cv2.getPerspectiveTransform(pts1,pts2)
res = cv2.warpPerspective(img,M,(200,200))
plt.subplot(121)
plt.imshow(img,'Blues')
plt.subplot(122)
plt.imshow(res,'brg')
plt.show()