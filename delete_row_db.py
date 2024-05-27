import sqlite3

# データベースに接続
conn = sqlite3.connect('my_database.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# 特定の行を削除
cursor.execute('DELETE FROM locations WHERE id = 1')

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()
