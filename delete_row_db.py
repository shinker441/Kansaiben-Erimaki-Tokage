import sqlite3

# データベース接続オブジェクトを初期化
conn = None

try:
    # データベースに接続
    conn = sqlite3.connect(
        'C:\\Users\\kansh\\Documents\\TKU-春\\知識情報システム演習A\\work_file\\my_database.db')
    cursor = conn.cursor()

    # 特定の行を削除
    cursor.execute('DELETE FROM locations WHERE id = 8')

    # 変更をコミット
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn is not None:
        conn.close()
