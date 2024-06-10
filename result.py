import sqlite3
import random
import math
import json

# データベースからランダムに画像と緯度経度を取得する関数
def get_random_location(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT image_url, lat, lng FROM locations")
    locations = cursor.fetchall()
    conn.close()
    return random.choice(locations)

# ハバースインの公式を使用して距離を計算する関数
def haversine(lat1, lon1, lat2, lon2):
    R = 6371e3  # 地球の半径 (メートル)
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)
    
    a = math.sin(Δφ / 2) * math.sin(Δφ / 2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2) * math.sin(Δλ / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

# データベースのパス
db_path = 'path/to/your/database.db'

# ランダムに選択された画像とその緯度経度を取得
image_url, initial_lat, initial_lng = get_random_location(db_path)
print(f"Selected image: {image_url}, Latitude: {initial_lat}, Longitude: {initial_lng}")

# 例として、ストリートビューの最終位置を指定
final_lat = 36.110521
final_lng = 140.101199

# 距離を計算
distance = haversine(initial_lat, initial_lng, final_lat, final_lng)
print(f"Distance: {distance} meters")

# 結果をJSONファイルに保存
result = {
    "image_url": image_url,
    "initial_lat": initial_lat,
    "initial_lng": initial_lng,
    "final_lat": final_lat,
    "final_lng": final_lng,
    "distance": distance
}

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)

print("Result saved to result.json")
