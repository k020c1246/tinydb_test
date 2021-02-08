from tinydb import TinyDB
db = TinyDB("db.json")
# インメモリーで使いたい時は
# from tinydb.storages import MemoryStorage
# db = TinyDB(stroage = MemoryStorage)

db.insert({"data":"value"})
print(db.all())
#[{"data":"value"}]
print("---")

# テーブルを全て消す
db.truncate()

# すべて表示する
for item in db:
    print(item)
print("---")
