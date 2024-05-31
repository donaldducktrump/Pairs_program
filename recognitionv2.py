import cv2
import pytesseract
from PIL import Image

# Tesseractのパスを設定（Windowsの場合）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 画像を読み込み
image_path = R'C:\Users\kazut\OneDrive\Documents\Pairs\20231129_235425.png'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OCRを実行してテキストとその位置を取得
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, lang='jpn')

# テキストの位置を探す
is_hajimemashite = False
for i, text in enumerate(data['text']):
    if text == '21':
        x_21, y_21 = data['left'][i], data['top'][i]
    elif text == 'よろ' and i + 4 < len(data['text']) and \
         data['text'][i + 1] == 'し' and data['text'][i + 2] == 'く' and \
         data['text'][i + 3] == 'お' and data['text'][i + 4] == '願' and \
         data['text'][i + 7] == '大':
        is_hajimemashite = True
        x_ha, y_ha = data['left'][i], data['top'][i]
    elif text == '大' and i + 4 < len(data['text']) and \
         data['text'][i + 1] == '学' and data['text'][i + 2] == '三' and \
         data['text'][i + 3] == '年' and data['text'][i + 4] == '生' and \
         data['text'][i -7] == 'よろ':
        is_yorosiku = True
        x_ha, y_ha = data['left'][i], data['top'][i]
    
# はじめましてがある場合、21の左にある丸の色を分析
if is_hajimemashite and 'x_21' in locals():
    # 丸の色を分析（範囲や位置は調整が必要）
    circle_color = image[y_21+8, x_21-17]  # 21の左16、下16ピクセルの位置
    # circle_radius = 16
    # circle_image = image[y_21 :y_21 + circle_radius, x_21 - 22:x_21-12 ]

    cv2.imwrite("circle.png", circle_color)
    # 色をBGRからRGBに変換
    circle_color = circle_color[::-1]
    # 色の成分をint型に変換
    r, g, b = map(int, circle_color)

    # average_color = circle_image.mean(axis=(0, 1))
    # r, g, b = map(int, average_color)
    # 色の判定（灰色か黄色か緑色か）
    # gray_threshold = 20  # 灰色の閾値
    # yellow_threshold = 60  # 黄色の閾値
    # green_threshold = 60  # 緑色の閾値

    
    # is_gray = abs(r - g) < gray_threshold and abs(g - b) < gray_threshold and abs(b - r) < gray_threshold
    # is_yellow = r > yellow_threshold and g > yellow_threshold and b < yellow_threshold
    # is_green = g > r + green_threshold and g > b + green_threshold

    if r==1 and g==203 and b==111:
        print("丸は緑色です")
    elif r==243 and g==210 and b==58:
        print("丸は黄色です")
    elif r==191 and g==207 and b==207:
        print("丸は灰色です")
    else:
        print("丸の色は灰色でも黄色でも緑色でもありません")

    # if is_gray:
    #     print("丸は灰色です")
    # elif is_yellow:
    #     print("丸は黄色です")
    # elif is_green:
    #     print("丸は緑色です")
    # else:
    #     print("丸の色は灰色でも黄色でも緑色でもありません")

   
else:
    print("条件を満たすテキストが見つかりませんでした")
