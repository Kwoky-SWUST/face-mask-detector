import pandas as pd
import cv2
 
for n in range(1,1000):#正样本的数量1000张就是1,1000
    path='\\图片路径\\'+str(n)+'.jpg' #正样本的路径
    # 读取图片
    img = cv2.imread(path)
    img=cv2.resize(img,(50,50))
    cv2.imwrite('\\输出路径\\' + str(n) + '.jpg', img) #输出路径
    n += 1

