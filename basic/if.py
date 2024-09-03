# if文

#age = 20
#age_alcohol = 21
#if age >= age_alcohol:
#    print("You can drink beer!")
#else:
#    print("You are too yonng to drink beer")

#age_drive = 18

#if age >= age_alcohol:
#    print("You can drink beer!")
#elif age < age_drive:
#    print("You can't even drive")
#else:
#    print("You are not allowed to drink beer but you can drive only if you have a driver's licence")

#if not 0 < age < 120:
#    print("The value is invalid!!")

# challenge1

# もしbalanceがwithdrawより大きい場合、balanceを更新する
# if balance >= withdraw:
#    balance = balance - withdraw
#    print(balance)
# そうでなければ、引き出せないというエラーメッセージを表示させる
# else:
#    print("you can't withdraw because withdraw is bigger than balance'")

# challenge2
balance = 2000  # 残高
withdraw = 500  # 引き出し額
withdraw_limit = 10000000  # 引き出し上限額
# もしwithdrawがwithdraw_limitより大きい場合、引き出し上限エラーを出す
if withdraw > withdraw_limit:
    print("You can't withdraw because withdraw is bigger than withdraw_limit")
    print("The withdrawal_limit is {}".format(withdraw_limit))
# もしwithdrawがbalanceを上回っている場合、引き出しエラーを出す
elif withdraw > balance:
    print("you can't withdraw because you don't have a money")
# balanceを更新する
else:
    balance -= withdraw
    print("Your new balance is {}".format(balance))


