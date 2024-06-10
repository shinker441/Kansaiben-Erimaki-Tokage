import sqlite3

# データベースに接続
conn = sqlite3.connect(
    'C:\\Users\\kansh\\Documents\\TKU-春\\知識情報システム演習A\\work_file\\my_database.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# 実際の画像と位置情報を挿入
images = [
    ('images/image5.png', 36.105524, 140.101975),
    ('images/image6.png', 36.117091, 140.098686),
    ('images/image7.png', 36.102777, 140.105537),
    ('images/image8.png', 36.111237, 140.100129),
    ('images/image9.png', 36.112208, 140.099099),
    ('images/image10.png', 36.104164, 140.105966),
    ('images/image11.png', 36.109711, 140.104593),
    ('images/image12.png', 36.112416, 140.104335),
    ('images/image13.png', 36.085854, 140.106653),
    ('images/image14.png', 36.086687, 140.105279),
    ('images/image15.png', 36.108324, 140.102361),
    ('images/image16.png', 36.097229, 140.104249),
    ('images/image17.png', 36.098477, 140.104078),
    ('images/image18.png', 36.100003, 140.103477),
    ('images/image19.png', 36.102985, 140.103391),
    ('images/image20.png', 36.109573, 140.100988),
    ('images/image21.png', 36.100835, 140.103649),
    ('images/image22.png', 36.104441, 140.102533),
    ('images/image23.png', 36.085438, 140.107425),
    ('images/image24.png', 36.109573, 140.100129),
    ('images/image25.png', 36.111237, 140.100902),
    ('images/image26.png', 36.113802, 140.101331),
    ('images/image27.png', 36.112069, 140.099443),
    ('images/image28.png', 36.118309, 140.098155),
    ('images/image29.png', 36.103886, 140.104507),
    ('images/image30.png', 36.110682, 140.105365),
    ('images/image31.png', 36.110682, 140.105794),
    ('images/image32.png', 36.112277, 140.099271),
    ('images/image33.png', 36.094871, 140.104593),
    ('images/image34.png', 36.093276, 140.103391)
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
