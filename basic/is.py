# is演算子：同じオブジェクトかどうかを判定する
a = 1
b = 1
c = 3
d = a
e = 2 - 1
print(id(1))
print(id(a))
print(id(b))
print(a is b)
print(id(c))
print(a is c)
print(a is not c)
print(id(d))
print(d is a)
print(d is b)
print(id(e))
print(a is e)

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"  # "hello"
print(hello, hello2)
print(hello is hello2)
hello = "konnichiwa"
print(hello)
print(hello is hello2)

#  Noneかどうかの判定によく使う

nothing = None
print(None)
print(nothing is None)
print(id(nothing))
print(id(None))
