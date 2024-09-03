# Challenge1:「ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する。カジノに入ったらゲームを選べるようにする。選択できるゲームは
# 1:ルーレット、2:ブラックジャック、3:ポーカー、選択後、ゲーム内容をprint()する」
# 上記のコードを、1～3以外の文字が入力されたら再度ゲームを選べるようにrefactoringする

age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを1～3の中から選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""
if age >= casino_age:
    print("どうぞ、お入りください!!")
    while True:
        game = input(game_text)
        if game == "1":
            print("あなたは{}のルーレットを選びました！".format(game))
            break
        elif game == "2":
            print("あなたは{}のブラックジャックを選びました！".format(game))
            break
        elif game == "3":
            print("あなたは{}のポーカーを選びました！".format(game))
            break
        else:
            print("1～3を選択してください")
else:
    print("18歳未満の方はカジノへ入れません!!")

