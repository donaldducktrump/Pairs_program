import cv2
import pytesseract
import os
import datetime
import matplotlib.pyplot as plt
# import japanize_matplotlib
import time

# Tesseractのパスを設定（Windowsの場合）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 分析結果を記録するリスト
timestamps = []
colors = []
err_timestamps = []

# 1時間の監視
end_time = datetime.datetime.now() + datetime.timedelta(hours=48)
while datetime.datetime.now() < end_time:
    current_minute = datetime.datetime.now().replace(second=0, microsecond=0)
    formatted_time = current_minute.strftime("%Y%m%d_%H%M")
    print(f"現在の時刻: {current_minute}")

    # # カレントディレクトリの全ファイルを逆順で走査
    # files = sorted(os.listdir('.'), reverse=True)
    # image_found = False
    # for file in files:
    #     print(f"チェック中のファイル: {file}")
    #     if file.startswith(formatted_time) and file.endswith('.png'):
    #         image_name = file
    #         print(f"見つかった画像ファイル: {image_name}")
    #         image_found = True
    #         break
    # カレントディレクトリのファイルを逆順で走査
    files = sorted(os.listdir('.'), reverse=True)
    latest_file = None
    for file in files:
        print(f"チェック中のファイル: {file}")
        if file.endswith('.png') and file.startswith(formatted_time[:11]):  # 年月日_時分まで一致するファイルを探す
            latest_file = file
            print(f"見つかった画像ファイル: {latest_file}")
            break

    if latest_file:
        print(f"見つかった画像ファイル: {latest_file}")
        # 画像を読み込む
        image = cv2.imread(latest_file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # ここにOCRと色分析のコードを追加



        # OCRを実行してテキストとその位置を取得
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, lang='jpn')

        # テキストの位置を探す
        is_hajimemashite = False
        is_yorosiku = False
        for i, text in enumerate(data['text']):
            if text == '21':
                x_21, y_21 = data['left'][i], data['top'][i]
            elif text == 'よろ' and i + 4 < len(data['text']) and \
                data['text'][i + 1] == 'し' and data['text'][i + 2] == 'く' and \
                data['text'][i + 3] == 'お' and data['text'][i + 4] == '願' and \
                data['text'][i -11] == '大':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-20], data['top'][i-20]
            elif text == '大' and i + 4 < len(data['text']) and \
                data['text'][i + 1] == '学' and data['text'][i + 2] == '三' and \
                data['text'][i + 3] == '年' and data['text'][i + 4] == '生' and \
                data['text'][i - 7] == 'よろ' and data['text'][i - 12] == '東京':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-14], data['top'][i-14]
            elif text == '大' and i + 4 < len(data['text']) and \
                data['text'][i + 1] == '学' and data['text'][i + 2] == '三' and \
                data['text'][i + 3] == '年' and data['text'][i + 4] == '生' and \
                data['text'][i - 7] == 'よろ' and data['text'][i - 11] == '東京':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-14], data['top'][i-14]
            elif text == '大' and i + 4 < len(data['text']) and \
                data['text'][i + 1] == '学' and data['text'][i + 2] == '三' and \
                data['text'][i + 3] == '年' and data['text'][i + 4] == '生' and \
                data['text'][i -7] == 'よろ' and data['text'][i - 10] == '東京':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-12], data['top'][i-12]
            elif text == '大' and i + 4 < len(data['text']) and \
                data['text'][i + 1] == '学' and data['text'][i + 2] == '三' and \
                data['text'][i + 3] == '年' and data['text'][i + 4] == '生' and \
                data['text'][i - 5] == '21' and data['text'][i - 1] != '21':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-5], data['top'][i-5]
            elif text == '学' and i + 4 < len(data['text']) and \
                data['text'][i - 1] == 'ます':
                is_yorosiku = True
                x_ha, y_ha = data['left'][i], data['top'][i]
                x_21, y_21 = data['left'][i-12], data['top'][i-12]
            
            
            

        # はじめましてがある場合、21の左にある丸の色を分析
        if is_yorosiku:
            # # 丸の色を分析（範囲や位置は調整が必要）
            circle_color = image[y_21+8, x_21-17]  # 21の左16、下16ピクセルの位置
            # 色をBGRからRGBに変換
            circle_color = circle_color[::-1]
            
            # 色の成分をint型に変換
            r, g, b = map(int, circle_color)

            # circle_radius = 16
            # circle_image = image[y_21 :y_21 + circle_radius, x_21 - 22:x_21-12 ]

            # average_color = circle_image.mean(axis=(0, 1))
            # r, g, b = map(int, average_color)
            # 色の判定（灰色か黄色か緑色か）
            # gray_threshold = 20  # 灰色の閾値
            # yellow_threshold = 60  # 黄色の閾値
            # green_threshold = 60  # 緑色の閾値

            # is_gray = abs(r - g) < gray_threshold and abs(g - b) < gray_threshold and abs(b - r) < gray_threshold
            # is_yellow = r > yellow_threshold and g > yellow_threshold and b < yellow_threshold
            # is_green = g > r + green_threshold and g > b + green_threshold

            if r==191 and g==207 and b==207:
                colors.append("gray")
                color = "gray"
            elif r==243 and g==210 and b==58:
                colors.append("yellow")
                color = "yellow"
            elif r==1 and g==203 and b==111:
                colors.append("green")
                color = "green"
            else:
                colors.append("Other")
                color = "black"
                err_timestamps.append(current_minute)

            # # 色の判定（灰色か黄色か緑色か）
            # if abs(r - g) < 10 and abs(g - b) < 10 and abs(b - r) < 10 and 100 <= r <= 200 and 100 <= g <= 200 and 100 <= b <= 200:
            #     colors.append('gray')
            # elif 50 <= circle_color[0] <= 255 and 200 <= circle_color[1] <= 255 and 50 <= circle_color[2] <= 255:
            #     colors.append('yellow')
            # elif 50 <= circle_color[0] <= 255 and 50 <= circle_color[1] <= 255 and 0 <= circle_color[2] <= 50:
            #     colors.append('green')
            # else:
            #     colors.append('Other')
        else:
            colors.append("N/A")
            err_timestamps.append(current_minute)
            
        timestamps.append(current_minute)

        today = datetime.date.today()
        
        # 以前のコード部分は変更せずに続けます...

        # 色ごとに色コードを割り当てる
        color_codes = []
        for color in colors:
            if color == "gray":
                color_codes.append('#808080')  # 灰色
            elif color == "yellow":
                color_codes.append('#FFFF00')  # 黄色
            elif color == "green":
                color_codes.append('#008000')  # 緑色
            else:
                color_codes.append('#000000')  # 該当しない場合は黒色

        # 時系列データを基にグラフを作成
        plt.figure(figsize=(10, 6))
        plt.scatter(timestamps, colors, c=color_codes, label='Color of the circle')  # y値は仮に1に設定
        plt.xlabel('Time')
        plt.ylabel('Color')
        plt.title('1hour')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        # plt.show()

        # グラフを画像として保存
        plt.savefig(f'color_analysis_results_3_{today.strftime("%Y%m%d")}.png')
        # plt.close()

        # その後のコード...

                    
        # # 時系列データを基にグラフを作成
        # plt.figure(figsize=(10, 6))
        # plt.scatter(timestamps, colors, c=color, label='Color of the circle')
        # plt.xlabel('Time')
        # plt.ylabel('Color')
        # plt.title('1hour')
        # plt.legend()
        # plt.xticks(rotation=45)
        # plt.tight_layout()
        # # plt.show()

        # # グラフを画像として保存
        # plt.savefig(f'color_analysis_results_{today.strftime('%Y%m%d')}.png')
        # # plt.close()
                
        
    else:
        print(f"適切なファイルが見つかりませんでした。次のループに移ります。")

    # 1分待機
    print(err_timestamps)
    time.sleep(60)


