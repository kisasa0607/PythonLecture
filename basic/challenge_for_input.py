# input(): ユーザの入力した値(文字列)を取得する

# Challenge1:ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する
# Challenge2:カジノに入ったらゲームを選べるようにする.　選択できるゲームは3種類で、選択後、ゲーム内容をprint()する
age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
4: ソリティア
"""
if age >= casino_age:
    print("どうぞ、お入りください!!")
    game = input(game_text)
    if game == "1":
        print("あなたは{}のルーレットを選びました！".format(game))
    elif game == "2":
        print("あなたは{}のブラックジャックを選びました！".format(game))
    elif game == "3":
        print("あなたは{}のポーカーを選びました！".format(game))
    elif game == "4":
        print("あなたは{}のソリティアを選びました！".format(game))
    else:
        print("1～4を選択してください")
else:
    print("18歳未満の方はカジノへ入れません!!")


