# forループ

# fruits = ['apple', 'peach', 'melon', 'grapes']
#
# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iterationとiterable

# Challenge1：ユーザに好きなフルーツを入力してもらい、fruitsリストの各フルーツに対して「好き/好きじゃない」をprint()する
# fruits = ['apple', 'peach', 'melon', 'grapes']
# favorite = input("あなたの好きなフルーツは？")
# for fruit in fruits:
#     if favorite == fruit:
#         print(f"{fruit}は好き")
#     else:
#         print(f"{fruit}は好きじゃない")

# Challenge2：fruitsリストの各フルーツに対して、「好き/好きじゃない」をユーザに聞いて、好きなフルーツリスト、好きじゃないフルーツリストを作成する
fruits = ['apple', 'peach', 'melon', 'grapes']
favorite_fruits = []
non_favorite_fruits = []
for fruit in fruits:
    favorite = input(f"{fruit}は好きですか？　y/n")
    if favorite == "y":
        favorite_fruits.append(fruit)
    else:
        non_favorite_fruits.append(fruit)
if len(favorite_fruits) == 0:
    print(f"好きなフルーツは1つもありません")
else:
    print(f"好きなフルーツは{favorite_fruits}です！")
if len(non_favorite_fruits) == 0:
    print(f"好きじゃないフルーツは1つもありません")
else:
    print(f"好きじゃないフルーツは{non_favorite_fruits}です")
