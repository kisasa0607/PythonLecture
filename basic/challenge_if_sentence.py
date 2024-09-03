# if文演習

# challenge2
balance = 500000  # 残高
withdraw_limit = 1000000  # 引き出し上限額

while True:
    # 引き出し額をシステムに入力
    withdraw = int(input("引き出し額を入力してください"))

    # もし引き出し額が引き出し上限額より大きい場合、引き出し上限エラーを出す
    if withdraw > withdraw_limit:
        print("引き出し額が引き出し上限額を超えています")
        print("引き出し上限額は {}となります".format(withdraw_limit))
    # もし引き出し額が口座残高を上回っている場合、引き出しエラーを出す
    elif withdraw > balance:
        print("引き出し額が口座残高を上回っているため、口座から引き出せません")
    # 入力された額を引き出して口座残高を更新する
    else:
        balance -= withdraw
        print("あなたの口座残高は {}となります".format(balance))
        break


