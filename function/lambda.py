# 通常の関数
# def power(x):
#     return x * x

# lambda関数
# ※普通はlambdaを変数には格納しない
# p = lambda x: x * x

# print(power(4))  # -> 16
# print(p(4))  # -> 16

# lambda関数をreturnするケース

def square(x):
    return x * x

s = lambda x: x * x

print(square(3))
print(s(5))

def power(exponent):
    return lambda base: base ** exponent

third_power = power(3)
print(third_power(2))

# 引数にlambda関数を入れるケース
numbers = [6, 2, 5, 43, 5, 36, 67, 2]
filtered_nums = filter(lambda x: x % 2, numbers)
for num in filtered_nums:
    print(num)