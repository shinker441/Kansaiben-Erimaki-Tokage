<?php
// CORSヘッダーを追加
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

// データベースファイルへのパス
$dbfile = 'my_database.db';

// データベース接続を開く
$db = new SQLite3($dbfile);

// ランダムに画像と位置情報を取得するクエリを実行
$sql = "SELECT image_url, lat, lng FROM locations ORDER BY RANDOM() LIMIT 1";
$result = $db->query($sql);

// 結果を取得してJSON形式で出力
if ($row = $result->fetchArray(SQLITE3_ASSOC)) {
    echo json_encode($row);
} else {
    echo json_encode([]);
}

// データベース接続を閉じる
$db->close();
