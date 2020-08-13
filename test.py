import cgi # CGIモジュールのインポート
import sys

form = cgi.FieldStorage() # フォームデータを取得する

print("Content-Type: text/html; charset=UTF-8") # HTMLを記述するためのヘッダ
print("")

# フォームのデータが入力されていない場合
# if "birthday" not in form:
#     print("<h1>Error!</h1>")
#     print("<br>")
#     print("テキストを入力してください！")
#     print("<a href='/'><button type='submit'>戻る</button></a>")
#     sys.exit()

birthday = form.getvalue("birthday") # データの値を取得する

print(birthday)

