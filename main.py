# R：「こんにちわ,私の名前は roboter です。あなたの名前は？」とターミナルに表示しユーザーの名前入力を促す。
# U: ターミナル上で[ユーザー名]を入力する
# 入力(string)roboter
# 出力(string)ユーザーの名前を入力してもらう
# R：「こんにちわ,私の名前は roboter です。あなたの名前は？」とターミナルに表示しユーザーの名前入力を促し
# ユーザーにターミナル上で[ユーザー名]を入力してもらう。


def greeting():
    return input("「こんにちわ,私の名前は roboter です。あなたの名前は？」\n名前を入力してください:  >>  ")


greeting()


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


favorite_restaurant()


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


hear_recommendations()


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


another_favorite_restaurant()


# - [yes の場合](データベースで管理)
#   R:「ユーザー名さんのおすすめレストランはありますか？」とターミナル表示しユーザーの（おすすめのレストラン名）入力を促す。
# 入力(str)ユーザー名
# 出力(str)おすすめレストラン名の入力してもらう


def another_hear_recommendations_yes():
    input("「{0}さんのおすすめレストランはありますか？」\n>>   ".format("ユーザー"))


another_hear_recommendations_yes()


# - [no の場合]
#   R:「ユーザー名さんのおすすめレストランはありますか？」とターミナル表示しユーザーの（おすすめのレストラン名）入力を促す。
# 入力(str)ユーザー名
# 出力(str)おすすめレストラン名の入力してもらう


def another_hear_recommendations_no():
    input("「{0}さんのおすすめレストランはありますか？」\n>>   ".format("ユーザー"))


another_hear_recommendations_no()


# - 「ユーザー名さん。ありがとうございました。良い一日を。」とターミナルに表示する。
# 入力(str)ユーザー名
# 出力(str)「ありがとうございました。良い一日を。」とターミナルに表示する。

def last_greeting():
    print("「{0}さん。ありがとうございました。良い一日を。」".format("ユーザー"))


last_greeting()
