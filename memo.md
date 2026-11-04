## 1-1
Gitに不慣れだと難しい

## 2-5
文字列の変数   35行目（例: date = sys.argv[1]）
数の変数       50行目（例: len(todays)）
リストの変数   10行目（例: events = json.load(f)）

関数1   名前: load_schedule  
        受け取るもの: なし
        返すもの: リストの変数
        役割: jsonファイルの中身の取得
関数2   名前: filter_by_date
        受け取るもの: リストの変数、実行引数の日付
        返すもの: リストの変数
        役割: 全体リストから、指定日付が一致するデータのリストを日付順でソートして返す
関数3   名前: format_event
        受け取るもの: リストの変数
        返すもの: 文字列の変数
        役割: リストの内容を文字列フォーマットに整形し、その文字列を返す


## 第3回 午前
1ページ開いたときの往復の数（およそ）: 9 回
curl -I の1行目: HTTP/2 200
無いページの1行目: HTTP/2 404
API の full_name: https://api.github.com/repos/Tatsuzawa-Tomohito/reskilling-practice
    pushed_at: 2026-11-04T07:08:39Z