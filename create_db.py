import sqlite3

# データベースに接続（存在しない場合は作成されます）
conn = sqlite3.connect('my_database.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''
CREATE TABLE locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_url TEXT NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL
)
''')

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()
