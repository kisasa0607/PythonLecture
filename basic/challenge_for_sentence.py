
# 現在のバスケット内のフルーツ一覧
fruits = ['apple', 'peach', 'melon', 'grapes']
favorite_fruits = []
non_favorite_fruits = []
# バスケット内のフルーツを見せ、好きなフルーツがあれば、お気に入りカートに追加する
for fruit in fruits:
    favorite = input(f"{fruit}は好きですか？　好きであれば「y」を、好きでなければ「n」を入力してください")
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
