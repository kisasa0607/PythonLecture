# range(start, stop, step)
# for _ in range(10):
#     print("hello")

# Challenge:FizzBuzzゲームを作ろう！
# 1～50の数字をそれぞれprint()して、3の倍数で「Fizz」5の倍数で「Buzz」、3と5の倍数で「FizzBuzz」をprint()する
for i in range(1,51):
    print(i)
    if (i % 3 == 0) & (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print("Others")
