#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 入力画像を読み込み
img = cv2.imread('google.png')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 方法2(OpenCVで実装)
dst = cv2.Canny(gray, 100, 200)

# 結果を出力
cv2.imwrite("output.png", dst)