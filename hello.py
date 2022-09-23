import numpy
import cv2

# 画像データを入れる numpy.ndarray オブジェクト
image = numpy.zeros((256, 256, 3), numpy.uint8)

# テキストを描画する
text = "Hello, world!!"
org = (0, 100)
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.0
color = (0, 127, 0) # Blue, Green, Red
thickness = 1
line_type = cv2.LINE_AA
cv2.putText(image, text, org, font_face, font_scale, color, thickness, line_type)

# 画像を出力する
path = "hello-world.png"
cv2.imwrite(path, image)