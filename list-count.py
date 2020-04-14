
# import collections

string = [
    "nissan",
    "toyota",
    "nissan",
    "suzuki",
    "daihatu",
    "toyota",
    "toyota",
    "suzuki"]
count = {'nissan': 0, 'toyota': 0, 'suzuki': 0, "daihatu": 0}
# impot collectionsをインポートしリストに対してcollections.Counter()を実行すると
# ターミナルにCounter({})ができてキーとcount数が表示される。
# c = collections.Counter(string)
# print(c)
for string in string:
    count[string] += 1
    # print(count)
    # ",".join()で区別し文字列に
    changes = ",".join(count)
    # str.titleで単語毎に大文字へ
    print(str.title(changes))
    break
