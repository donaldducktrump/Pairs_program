import os
from datetime import datetime

# 変更したいファイルがあるディレクトリ
directory = R'C:\Users\kazut\OneDrive\Documents\Pairs'

# # ディレクトリ内の全ファイルに対して処理
# for filename in os.listdir(directory):
#     if filename.startswith("screenshot_") and filename.endswith(".png"):
#         # タイムスタンプをファイル名から抽出
#         timestamp = int(filename.split('_')[1].split('.')[0])

#         # タイムスタンプを日時に変換
#         date_time = datetime.fromtimestamp(timestamp)

#         # 新しいファイル名をフォーマット
#         new_filename = date_time.strftime("%Y-%m-%d_%H-%M-%S.png")

#         # 元のファイルパス
#         old_file = os.path.join(directory, filename)

#         # 新しいファイル名
#         new_file = os.path.join(directory, new_filename)

#         # ファイル名を変更
#         os.rename(old_file, new_file)

# ディレクトリ内の全ファイルに対して処理
for filename in os.listdir(directory):
    if filename.startswith("2023-11-29") and filename.endswith(".png"):

        new_filename = filename.replace("-","")

        # 元のファイルパス
        old_file = os.path.join(directory, filename)

        # 新しいファイル名
        new_file = os.path.join(directory, new_filename)

        # ファイル名を変更
        os.rename(old_file, new_file)
