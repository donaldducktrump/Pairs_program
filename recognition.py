import cv2
import pytesseract
from PIL import Image

# 画像のパス
image_path = R'C:\Users\kazut\OneDrive\Documents\Pairs\20231203_171022.png'

# Tesseractのパスを設定pi（Windowsの場合）
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 画像を読み込み
print("画像を読み込みます")
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # コントラストを向上させる
# # alpha: コントラスト制御（1.0以上でコントラストが増加）
# # beta: 明るさ制御（正の値で明るくなる）
# enhanced = cv2.convertScaleAbs(gray, alpha=1.5, beta=50)
# # contrast_img = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

# # 二値化
# _, binary = cv2.threshold(enhanced, 180, 255, cv2.THRESH_BINARY)

# # ノイズの除去
# denoised_img = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)
# processed_img = Image.fromarray(denoised_img)

# OCRを実行してテキストとその位置を取得
print("OCRを実行します")
data = pytesseract.image_to_data(gray, lang='jpn', output_type=pytesseract.Output.DICT)

# テキストデータの確認
print("見つかったテキスト:", data['text'])

# '21歳 東京' の位置を探す
found = False
for i in range(len(data['text'])):
    if '21歳' in data['text'][i] and '東京' in data['text'][i + 1]:
        found = True
        # テキストの位置を取得
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

        # テキストの左側の丸の色を分析（範囲や位置は調整が必要）
        # ここでは、xの左20ピクセル、yの中央にある色を分析
        circle_color = image[y + h // 2, x - 20]

        # 色をBGRからRGBに変換
        circle_color = circle_color[::-1]

        # 緑色か黄色かを判定（色の範囲は調整が必要）
        if 50 <= circle_color[0] <= 255 and 50 <= circle_color[1] <= 255 and 0 <= circle_color[2] <= 50:
            print("丸は緑色です")
        elif 50 <= circle_color[0] <= 255 and 50 <= circle_color[1] <= 255 and 50 <= circle_color[2] <= 255:
            print("丸は黄色です")
        else:
            print("丸の色は緑色でも黄色でもありません")
        break

if not found:
    print("'21歳 東京' が見つかりませんでした")