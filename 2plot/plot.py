import cv2
import numpy as np
from matplotlib import pyplot as plt
#绘制直线
#灰色
img = np.zeros((512,512),np.uint8)#生成一个空灰度图像
cv2.line(img,(0,0),(511,511),255,5)
plt.imshow(img,'gray')
#plt.show()
cv2.imwrite('line_gray.png',img)
#彩色
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.line(img,(0,0),(511,511),(0,255,0),5)
plt.imshow(img,'brg')
#plt.show()
cv2.imwrite('line_brg.png',img)
#绘制矩形
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.rectangle(img,(20,20),(411,411),(0,255,0),5)
plt.imshow(img,'brg')
#plt.show()
cv2.imwrite('rectangle_brg.png',img)
#绘制圆形
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.circle(img,(200,200),50,(0,0,255),8)#修改最后一个参数线粗
plt.imshow(img,'brg')
cv2.imwrite('circle_brg.png',img)
#绘制椭圆
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.ellipse(img,(256,256),(100,150),0,10,300,(0,255,255),-1)
#注意最后一个参数-1，表示对图像进行填充，默认是不填充的，如果去掉，只有椭圆轮廓了
plt.imshow(img,'brg')
#plt.show()
cv2.imwrite('ellipse_brg.png',img)
