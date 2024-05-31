import cv2
import pytesseract
import os
import datetime
import matplotlib.pyplot as plt
# import japanize_matplotlib
import time
import csv
import matplotlib.dates as mdates
import selenium
from itertools import groupby
from operator import itemgetter
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import base64


import time
import pyautogui
from PIL import Image
from PIL import ImageGrab

import base64

# Chrome WebDriverのパスを設定

driver_path = R'C:\Users\kazut\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=driver_path) 
driver = webdriver.Chrome(service=service)
# 開きたいウェブページのURL
driver.get('https://pairs.lv/search')


# def save_screenshot(driver, file_path, is_full_size=False):
#     # 画面サイズの取得
#     page_rect = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
#     # スクリーンショット設定
#     screenshot_config = {
#         # Trueの場合スクロールで隠れている箇所も含める、Falseの場合表示されている箇所のみ
#         "captureBeyondViewport": True,
#         "clip": {
#         "width": page_rect["contentSize"]["width"],
#         "height": page_rect["contentSize"]["height"],
#         "x": 1400,
#         "y": 100,
#         "scale": 25,
#     },
#     }
#     # スクリーンショット取得
#     base64_image = driver.execute_cdp_cmd("Page.captureScreenshot", screenshot_config)

#     # ファイル書き出し
#     with open(file_path, "wb") as fh:
#         fh.write(base64.urlsafe_b64decode(base64_image["data"]))


while True:
    # # ページをリフレッシュ
    # driver.refresh()
    # time.sleep(5)  # ページが完全にロードされるのを待つ

    # # スクリーンショットを撮る
    # now = datetime.datetime.now()
    # formatted_time = now.strftime('%Y%m%d_%H%M%S')
    # # screenshot = pyautogui.screenshot()
    # screenshot_path = f'{formatted_time}.png'
    # driver.save_screenshot( f'{formatted_time}.png')
    # # screenshot.save(f'{formatted_time}.png')
    # # cropped = screenshot.crop((1100, 400, 2000, 1400)) # 切り取る範囲 full screen,175% zoom
    # # cropped.save(f'{formatted_time}.png')
    #     # PILを使用して画像を開く
    # img = Image.open(screenshot_path)

    # # 画像サイズを取得して中央2/3の範囲を計算
    # width, height = img.size
    # left = width / 3.5  # 左端から1/6の位置
    # top = height / 6  # 上端から1/6の位置
    # right = width - left*4/2.8  # 右端から1/6の位置
    # bottom = height - top*6/9  # 下端から1/6の位置

    # # 指定した範囲を切り取る
    # cropped_img = img.crop((left, top, right, bottom))

    # # 切り取った画像を保存
    # cropped_img.save(screenshot_path)




    # 1分待機
    # time.sleep(55)
# Tesseractのパスを設定（Windowsの場合）
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # 分析結果を記録するリスト
    timestamps = []
    colors = []
    err_timestamps = []
    color_codes = []
    # # CSVファイルから読み込み
    # try:
    #     with open('data.csv', 'r') as file:
    #         reader = csv.reader(file)
    #         next(reader)  # ヘッダーをスキップ
    #         for row in reader:
    #             timestamps.append(row[0])
    #             colors.append(row[1])
    #             color_codes.append(row[2])
    # except FileNotFoundError:
    #     print("ファイルが存在しません。新しくデータを生成します。")

    # CSVファイルからデータを読み込む
    try:
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダーをスキップ
            for row in reader:
                timestamp = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')  # タイムスタンプをdatetimeに変換
                color = row[1]
                color_code = row[2]
                timestamps.append(timestamp)
                colors.append(color)
                color_codes.append(color_code)
    except FileNotFoundError:
        print("ファイルが存在しません。新しくデータを生成します。")

    # 1時間の監視
    end_time = datetime.datetime.now() + datetime.timedelta(hours=216)
    while datetime.datetime.now() < end_time:
                # ページをリフレッシュ
        driver.refresh()
        time.sleep(5)  # ページが完全にロードされるのを待つ

        # スクリーンショットを撮る
        now = datetime.datetime.now()
        formatted_time = now.strftime('%Y%m%d_%H%M%S')
        # screenshot = pyautogui.screenshot()
        screenshot_path = f'{formatted_time}.png'
        driver.save_screenshot( f'{formatted_time}.png')
        # screenshot.save(f'{formatted_time}.png')
        # cropped = screenshot.crop((1100, 400, 2000, 1400)) # 切り取る範囲 full screen,175% zoom
        # cropped.save(f'{formatted_time}.png')
            # PILを使用して画像を開く
        img = Image.open(screenshot_path)

        # 画像サイズを取得して中央2/3の範囲を計算
        width, height = img.size
        left = width / 3.5  # 左端から1/6の位置
        top = height / 6  # 上端から1/6の位置
        right = width - left*4/2.8  # 右端から1/6の位置
        bottom = height - top*6/9  # 下端から1/6の位置

        # 指定した範囲を切り取る
        cropped_img = img.crop((left, top, right, bottom))

        # 切り取った画像を保存
        cropped_img.save(screenshot_path)

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
                if text == 'よろ' and i + 4 < len(data['text']) and \
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
                    data['text'][i - 10] == 'よろ' and data['text'][i - 15] == '東京':
                    is_yorosiku = True
                    x_ha, y_ha = data['left'][i], data['top'][i]
                    x_21, y_21 = data['left'][i-17], data['top'][i-17]
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
            
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['timestamp', 'color', 'color_codes'])  # ヘッダー
                for timestamp, color, color_codes in zip(timestamps, colors, color_codes):
                    writer.writerow([timestamp, color , color_codes])

                    # タイムスタンプを日付ごとにグループ化
            grouped_data = groupby(zip(timestamps, colors, color_codes), key=lambda x: x[0].date())

            # 各グループに対してCSVファイルを作成
            for date, group in grouped_data:
                filename = f'data_{date}.csv'
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['timestamp', 'color', 'color_codes'])  # ヘッダー
                    for timestamp, color, color_code in group:
                        writer.writerow([timestamp.strftime('%Y-%m-%d %H:%M:%S'), color, color_code])

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

            timestamps_str = [dt.strftime('%Y-%m-%d %H:%M:%S') if isinstance(dt, datetime.datetime) else dt for dt in timestamps]

            timestamps = [datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') if isinstance(ts, str) else ts for ts in timestamps]

            # 日付ごとにタイムスタンプをグループ化
            timestamps.sort()  # 必ず最初にソートする
            grouped = groupby(zip(timestamps, colors, color_codes), key=lambda x: x[0].date())
            if colors[-5:] == ["N/A","N/A","N/A","N/A","N/A"]:
                # SeleniumでWeb操作を実行
                driver.get("https://pairs.lv/search")

                # 特定の座標にマウスを移動してクリック
                # ここで指定する座標はページのレイアウトに依存します
                x_coordinate = 320  # X座標の値を指定
                y_coordinate = 80  # Y座標の値を指定
                action = ActionChains(driver)
                action.move_by_offset(x_coordinate, y_coordinate).click().perform()

                # WebDriverを閉じる
                # driver.quit()

            for date, group in grouped:
                group_list = list(group)
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # タイムスタンプ、色、色コードを抽出
                group_timestamps, group_colors, group_color_codes = zip(*group_list)
                
                # 散布図をプロット
                ax.scatter(group_timestamps, [1] * len(group_timestamps), c=group_color_codes, label='Color of the circle')
                
                # X軸のフォーマッタとロケータを設定
                ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # 1時間ごとの目盛り
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # 時:分 のフォーマットで表示

                            # タイトル、ラベル、凡例
                ax.set_title(f'Color Analysis for {date}')
                ax.set_xlabel('Time')
                ax.set_ylabel('Color')
                ax.legend()
                
                # x軸のラベルを回転
                plt.xticks(rotation=45)
                plt.tight_layout()

                # グラフを画像として保存
                plt.savefig(f'color_analysis_{date}.png')
                plt.close(fig)  # メモリの解放

            # # 時系列データを基にグラフを作成
            # plt.figure(figsize=(10, 6))
            # plt.scatter(timestamps_str, colors, c=color_codes, label='Color of the circle')  # y値は仮に1に設定
            # plt.xlabel('Time')
            # plt.ylabel('Color')
            # plt.title('216hour(-12/9)')
            # plt.legend()
            # plt.xticks(rotation=45)
            # plt.tight_layout()
            # # plt.show()

            # # グラフを画像として保存
            # plt.savefig(f'color_analysis_results_3_{today.strftime("%Y%m%d")}.png')
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


