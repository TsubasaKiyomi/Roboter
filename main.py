# R：「こんにちわ,私の名前は roboter です。あなたの名前は？」とターミナルに表示しユーザーの名前入力を促す。
# U: ターミナル上で[ユーザー名]を入力する
# 入力(string)roboter
# 出力(string)ユーザーの名前を入力してもらう
# R：「こんにちわ,私の名前は roboter です。あなたの名前は？」とターミナルに表示しユーザーの名前入力を促し
# ユーザーにターミナル上で[ユーザー名]を入力してもらう。


import csv


def greeting():
    return input("「こんにちわ,私の名前は roboter です。あなたの名前は？」\n名前を入力してください:  >>  ")


# R:「私のおすすめは（レストラン名） です。[ユーザー名]さんは,このレストランはお好きですか？」と
# [yes/no]」とターミナルに表示してユーザーの入力を待つ。
# 入力１(string)レストラン名
# 入力２(string)ユーザー名
# 出力　(boolean)：オススメのレストランが好きかどうか
# 「私のおすすめは（レストラン名） です。（[ユーザー名]）さんは,このレストランはお好きですか？
# [yes/no]」とターミナルに表示してユーザーの入力を待ち、ユーザーからのインプットがyesだった場合はtrue、noだった場合はfalse、それ以外の場合は質問を繰り返す。


def favorite_restaurant():
    while True:
        print(
            "「私のおすすめは{0}です。{1}さんは,この{0}はお好きですか？」\n".format(
                "japanes restaurant", "name"))
        answer = input("yes / no  >> ")
        if answer == "yes":
            True
            break
        elif answer == "no":
            False
            break


#     answers_deictinary = {
#         "y": "",
#         "Yes": "",
#         "YES": "",
#         "yes": "",
#         "n": "",
#         "No": "",
#         "NO": "",
#         "no": ""}
#     test = answers_deictinary[input("Yes/No >>")]
#     break
# print(test)


# - [yes だった場合]
#   R:「ユーザー名さんのおすすめレストランはありますか？」とターミナル表示しユーザーの（おすすめのレストラン名）入力を促す。
# 入力(str)ユーザー名
# 出力(str)おすすめレストラン名の入力してもらう


def hear_recommendations():
    input("「{0}さんのおすすめレストランはありますか？」\n>>   ".format("ユーザー"))
    return


# R:「私のおすすめは（レストラン名） です。[ユーザー名]さんは,このレストランはお好きですか？」と
# [yes/no]」とターミナルに表示してユーザーの入力を待つ。
# 入力１(string)    ：レストラン名
# 入力２(string)    ：ユーザー名
# 出力　(boolean)：オススメのレストランが好きかどうか
#  [no の場合]
#   R:「私のおすすめは（レストラン名） です。（[ユーザー名]）さんは,このレストランはお好きですか？」
# [yes/no]」とターミナルに表示してユーザーの入力を待ち、ユーザーからのインプットがyesだった場合はtrue、noだった場合はfalse、それ以外の場合は質問を繰り返す。


def another_favorite_restaurant():
    while True:
        print(
            "「私のおすすめは{0}です。{1}さんは,この{0}はお好きですか？」\n".format(
                "american restaurant", "ユーザー"))
        answer = input("yes / no  >> ")
        if answer == "yes":
            True
            break
        elif answer == "no":
            False
            break


# - [yes の場合](データベースで管理)
#   R:「ユーザー名さんのおすすめレストランはありますか？」とターミナル表示しユーザーの（おすすめのレストラン名）入力を促す。
# 入力(str)ユーザー名
# 出力(str)おすすめレストラン名の入力してもらう


def another_hear_recommendations_yes():
    input("「{0}さんのおすすめレストランはありますか？」\n>>   ".format("ユーザー"))


# - [no の場合]
#   R:「ユーザー名さんのおすすめレストランはありますか？」とターミナル表示しユーザーの（おすすめのレストラン名）入力を促す。
# 入力(str)ユーザー名
# 出力(str)おすすめレストラン名の入力してもらう


def another_hear_recommendations_no():
    input("「{0}さんのおすすめレストランはありますか？」\n>>   ".format("ユーザー"))


# - 「ユーザー名さん。ありがとうございました。良い一日を。」とターミナルに表示する。
# 入力(str)ユーザー名
# 出力(str)「ありがとうございました。良い一日を。」とターミナルに表示する。

def last_greeting():
    print("「{0}さん。ありがとうございました。良い一日を。」".format("ユーザー"))


# 入力したデータを[レストラン名] + [ユーザー人数] に分けて保存する。
# 入力(str)レストラン名
# 入力(int)レストランを選んだユーザー人数
# 入力したデータを[レストラン名] + [ユーザー人数] を書き込む


def writing():
    with open("data.csv", "w") as csv_file:
        fieldnames = ["restaurant_name", "count_number"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {"restaurant_name": "American_restaurant",
             "count_number": 3})
        writer.writerow(
            {"restaurant_name": "Japanese_restaurant",
             "count_number": 8})


# 入力したデータを[レストラン名] + [ユーザー人数] に分けて保存されたものを読み込む
# 出力1(str)レストラン名
# 出力２(int)レストランを選んだユーザー人数


def reading():
    with open("data.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["restaurant_name"], row["count_number"])


greeting()
favorite_restaurant()
hear_recommendations()
another_favorite_restaurant()
another_hear_recommendations_yes()
another_hear_recommendations_no()
last_greeting()
writing()
reading()
