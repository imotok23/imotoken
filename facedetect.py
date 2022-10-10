import sys
import numpy
import cv2

# コマンドライン引数を読む
if len(sys.argv) < 3:
  print("画像ファイルのパスを指定してください。")
  sys.exit(1)
input_image_path  = sys.argv[1]
output_image_path = sys.argv[2]

# 画像を読み込む
# アルファチャンネル付きに対応するため IMREAD_UNCHANGED を使う
input_image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)

# Haar 特徴ベースのカスケード分類器による物体検出の準備
# 顔検出用のカスケード分類器を使用
face_cascade_name = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_name)

# 顔を検出
faces = face_cascade.detectMultiScale(input_image)

# 出力画像データを入れるオブジェクト
# 入力画像データを出力画像データにコピー
output_image = numpy.copy(input_image)

for (x, y, w, h) in faces:

  # 検出した顔の座標を出力
  print("Face: [{} x {} from ({}, {})]".format(w, h, x, y))

  # 顔の位置に楕円を描画
  center = (x + w // 2, y + h // 2)
  size = (w // 2, h // 2)
  angle = 0
  startAngle = 0
  endAngle = 360
  color = (127, 0, 255, 255) # Blue, Green, Red, Alpha
  thickness = 4
  cv2.ellipse(output_image, center, size, angle, startAngle, endAngle, color, thickness)

# 画像を出力
cv2.imwrite(output_image_path, output_image)