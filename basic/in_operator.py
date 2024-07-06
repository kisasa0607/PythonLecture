# in演算子
fruits = ['apple', 'peach', 'melon', 'grapes']
# print('apple' in fruits)
# print('apple' not in fruits)
# print('lemon' not in fruits)
# print('h' in 'hello world')

# Challenge：ユーザに好きなフルーツを入力したもらい、そのフルーツがfruitsリストにあればそのフルーツを削除し、なければそのフルーツを追加するプログラムを作る
your_favorite_fruit = input("あなたが好きなフルーツを入力してください")
if your_favorite_fruit in fruits:
    print("フルーツリストからあなたの好きな{}を取り出します!".format(your_favorite_fruit))
    fruits.remove(your_favorite_fruit)
else:
    print("フルーツリストにあなたの好きな{}を追加します!".format(your_favorite_fruit))
    fruits.append(your_favorite_fruit)

print("今あるフルーツはこれらです！")
print(fruits)




