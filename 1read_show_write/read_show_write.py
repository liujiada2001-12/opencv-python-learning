#import cv2
#img = cv2.imread('light1.jpg')
#cv2.imshow('image',img) 
#cv2.waitKey(0) 
#cv2.destroyAllWindows()
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('light1.jpg',0);#打开为灰度图像
plt.imshow(img, 'gray') #必须规定为显示的为什么图像
plt.xticks([]),plt.yticks([]) #隐藏坐标线 
plt.show() #显示出来，不要也可以，但是一般都要了
cv2.imwrite('light1_gray.tif',img)