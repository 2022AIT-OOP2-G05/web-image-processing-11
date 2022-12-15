import cv2

# 画像の読み込み
img = cv2.imread("6632749D-F045-4866-89A2-88EDF54477E5.jpeg", 0)

# 閾値の設定
threshold = 100

ret2, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

#閾値がいくつになったか確認
print("ret2: {}".format(ret2))

#画像の確認
#cv2.imshow("otsu", img_otsu)
#cv2.waitKey()
#cv2.destroyAllWindows()

cv2.imwrite('opencv_2_cvtcolr.jpg', img_otsu)