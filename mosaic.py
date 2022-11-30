#ライブラリをインポート
import cv2

#画像読み込み
img = cv2.imread("kaoface.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_con = img.copy()

#モザイク関数
def mosaic(img, ratio=0.1):
    small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

#モザイクエリア
def mosaic_area(img, x, y, width, height, ratio=0.1):
    dst = img.copy()
    dst[y:y+height, x:x+width] = mosaic(dst[y:y+height, x:x+width], ratio)
    return dst

# カスケードファイル読み込み
cascade = cv2.CascadeClassifier(".\haarcascade_frontalface_alt2.xml")
#顔検出
faces = cascade.detectMultiScale(img_gray)
#検出した顔にモザイク処理
if len(faces) > 0:
    for face in faces:
        x, y, w, h =face
        img_con = mosaic_area(img_con,x, y, w, h)
#ファイル書き出し
cv2.imwrite("mosaic_face.jpg", img_con)