import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui
from PIL import Image
from PIL import ImageGrab
from datetime import datetime
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
    # ページをリフレッシュ
    driver.refresh()
    time.sleep(5)  # ページが完全にロードされるのを待つ

    # スクリーンショットを撮る
    now = datetime.now()
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




    # 1分待機
    time.sleep(55)


