import sqlite3

# データベースに接続
conn = sqlite3.connect('my_database.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# 実際の画像と位置情報を挿入
images = [
    ('images/test_image1.png', 36.08626942859437, 140.10662689565217),
    ('images/test_image2.png', 36.11043693209843, 140.1013432175039)
]

# データを挿入
for image_url, lat, lng in images:
    cursor.execute('''
    INSERT INTO locations (image_url, lat, lng)
    VALUES (?, ?, ?)
    ''', (image_url, lat, lng))

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()
