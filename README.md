# Roboter 機能一覧

## ユーザーインターフェース　（装置と人間との接点である、入出力部分）ユーザーとのやり取り部分

- 「こんにちわ,私の名前は roboter です.あなたの名前は？」とターミナルに表示しユーザーの入力を促す。
- roboter がおすすめするレストランは[（レストラン名を選んだユーザー数）]の数が大きいものからターミナルに表示する。
- 「私のおすすめは（レストラン名） です。このレストランはお好きですか？」とターミナルに表示する。
- おすすめしたレストランに対して好きかどうか「[yes/no]」入力を促す。
- 「（ユーザー名）さんのおすすめレストランはありますか？」とターミナル表示しユーザーの入力を促す。
- 「（ユーザー名）さん。ありがとうございました。良い一日を。」とターミナルに表示する。

## ユーザーインターフェースとデーターベースの中間処理

## データーベース

- ユーザーが入力したデータを [（レストラン名）] + [（同じレストラン名を入力したユーザー数）] に分ける。＃（[yse/no]）では増減しない

```
# collectionsでリスト内のキーの数を数える
import collections

# 変数名　= 「["レストラン名１","レストラン名２","レストラン名２",]」を入力する。
restaurant_name = ["restaurant１","restaurant２","restaurant３","restaurant１","restaurant２"]

# collections.Counter(変数名)で数えたキーを辞書型表示できる。
print(collections.Counter(restaurant_name))

```
