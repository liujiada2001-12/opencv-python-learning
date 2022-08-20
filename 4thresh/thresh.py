import cv2
import matplotlib.pyplot as plt

img = cv2.imread('light1.jpg',0) #直接读为灰度图像
#简单阈值
ret,thresh1 = cv2.threshold(img,130,255,cv2.THRESH_BINARY) #黑白二值
ret,thresh2 = cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV) #黑白二值反转
ret,thresh3 = cv2.threshold(img,130,255,cv2.THRESH_TRUNC) #多像素值
ret,thresh4 = cv2.threshold(img,130,255,cv2.THRESH_TOZERO) #
ret,thresh5 = cv2.threshold(img,130,255,cv2.THRESH_TOZERO_INV)
titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
#plt.show()

#自适应阈值
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
images = [img,th1,th2,th3]
plt.figure()
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#plt.show()
#Otsu’s二值化
#简单滤波
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Otsu 滤波
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.figure()
plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.hist(img.ravel(),256)#.ravel方法将矩阵转化为一维
plt.subplot(223),plt.imshow(th1,'gray')
plt.subplot(224),plt.imshow(th2,'gray')
#plt.show()
