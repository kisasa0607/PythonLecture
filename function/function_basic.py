# 関数（function）
# print()
# len()
# input()

# 華氏から摂氏に変換する
# fahrenheit = 72
# celsius = (fahrenheit - 32) * 5 / 9
# print(celsius)

# celsius = fahrenheit_to_celsius(fahrenheit)
fahrenheit = 80
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)



