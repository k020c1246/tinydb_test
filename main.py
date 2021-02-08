#モジュールのインポート
from tinydb import TinyDB, Query

#データベースの作成
db = TinyDB('sample.json')

#名前と年齢に関するデータの作成
#辞書型で挿入
db.insert({'name':'Bob', 'age':31})
db.insert({'name':'Jane', 'age':22})
db.insert({'name':'taichi','age':22})

#全データの取得
print(db.all())
'''[{'age': 31, 'name': 'Bob'}, {'age': 22, 'name': 'Jane'}]'''
print("---")

#複数渡すとき
dic_list = [{'name':'John', 'age':25}, {'name':'Elen', 'age':40}]
db.insert_multiple(dic_list)

#ループ処理
for item in db:
    print(item)
'''
{'name': 'Bob', 'age': 31}
{'name': 'Jane', 'age': 22}
{'name': 'John', 'age': 25}
{'name': 'Elen', 'age': 40}
'''
print("---")

#Queryオブジェクトを作成
que = Query()

#'name'=='Bob'のデータを検索
print("name == 'Bob'")
print(db.search(que.name == 'Bob'))
'''[{'age': 31, 'name': 'Bob'}]'''
print("---")

#条件式を指定できる
#'age'<30のデータを検索
print("age < 30")
print(db.search(que.age < 30))
'''[{'age': 22, 'name': 'Jane'}, {'age': 25, 'name': 'John'}]'''
print("---")

#ループ処理したいとき
for item in db.search(que.age < 30):
    print(item)
'''
{'name': 'Jane', 'age': 22}
{'name': 'John', 'age': 25}
'''
print("---")

print("age>30 のnameを表示")
for item in db.search(que.age>30):
    print(item["name"])
print("---")

print("nameがBobのageを表示")
# getは1件のみ
print(db.get(que.name=="Bob")["age"])
print("---")

#データの削除
print("age < 30 を削除")
db.remove(que.age < 30)
print("---")

#ループ処理
for item in db:
    print(item)
print("---")

print("すべて表示")
print(db.all())
print("---")

# すべて削除
# purgeは古いバージョンのもの
# db.purge()
db.truncate()
print(db.all())

