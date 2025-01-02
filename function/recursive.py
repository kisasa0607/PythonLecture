# 再帰関数 (recursive function): 関数内で自身の関数をcallする関数
# 一見大きく見える問題も，
# n! = n * (n-1) * (n-2) * ... * 1
# 小さい問題を繰り返すことで解決できる
# n! = n * (n-1)

def factrial(n):
    if n ==1:
        return 1
    else:
        return n * factrial(n-1)

print(factrial(2))

# challenge1
def fibonacci_recursive(n):

    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print(fibonacci_recursive(6))

# challenge2
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


# 再帰の方が時間がかかる
for i in range(6):
    print(i, fibonacci_recursive(i))
    # print(i, fibonacci(i))

