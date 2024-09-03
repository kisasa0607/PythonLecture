# if文演習

# challenge2
balance = 500000  # 残高
withdraw_limit = 1000000  # 引き出し上限額

#引き出し額をシステムに入力
withdraw = int(input("引き出し額を入力してください"))

# もしwithdrawがwithdraw_limitより大きい場合、引き出し上限エラーを出す
if withdraw > withdraw_limit:
    print("You can't withdraw because withdraw is bigger than withdraw_limit")
    print("The withdrawal_limit is {}".format(withdraw_limit))
# もしwithdrawがbalanceを上回っている場合、引き出しエラーを出す
elif withdraw > balance:
    print("you can't withdraw because you don't have a money")
# 入力された額を引き出してbalanceを更新する
else:
    balance -= withdraw
    print("Your new balance is {}".format(balance))


