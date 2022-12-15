import cv2 as cv

#カスケード分類器読み込み
HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(HAAR_FILE)

#画像の読み込み
img = cv.imread("sample.jpg")

#顔検出
face = cascade.detectMultiScale(img)

#顔部を枠で囲む
for x, y, w, h in face:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()