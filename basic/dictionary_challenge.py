age = int(input("何歳ですか？"))
casino_age = 18
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}
if age >= casino_age:
    print("どうぞ、お入りください!!")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")

        game_number = input(":")
        if game_number in game_dict.keys():
            print(f"あなたは{game_dict[game_number]}を選びました！")
            break
        else:
            print("正しい選択肢を選んでください")
else:
    print("18歳未満の方はカジノへ入れません!!")