import pandas as pd
import cv2
names=pd.read_excel('data\\imgName.xlsx')['names']# 读取所有照片名字,这里填入自己新建的Excel文件目录和名字
i=100000 #用于重新命名 
for imagepath in names:
    #读取图片
    img = cv2.imread(imagepath)
    #转成灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #人脸识别器
    detector = cv2.CascadeClassifier('haarcascades\\haarcascade_frontalface_default.xml')#这里是分类器的文件路径和名字
    #获取人脸位置
    faces = detector.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        #裁减图片
        gray = gray[y:y+h,x:x+w]  # 裁剪坐标为[y0:y1, x0:x1]
        #如果人脸不为空
        try:
            # 保存裁减后的灰度图
            cv2.imwrite('C:\\aaa\\mask\\gray1\\'+str(i)+'.jpg', gray)#输出处理后图片的文件夹位置
            # cv2.waitKey(3000)
            i += 1
        except:
            print()

