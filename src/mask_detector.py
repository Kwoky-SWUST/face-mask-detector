import cv2
detector= cv2.CascadeClassifier('C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')#人脸识别分类器
mask_detector=cv2.CascadeClassifier('D:\\facemask\\mask\\xml\\cascade.xml')#口罩识别分类器
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        face=img[y:y+h,x:x+w]
        mask_face=mask_detector.detectMultiScale(gray, 1.1, 5)
        for (x2,y2,w2,h2) in mask_face:
            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
    cv2.imshow('Mask Detector', img)
    cv2.waitKey(3)
cap.release()
cv2.destroyAllWindows()

