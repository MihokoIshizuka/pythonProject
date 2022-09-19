print('Hello World!')

# カンマ区切りで半角空いた出力ができる
print('Hello', 'paiza')

# print 関数を使うとデフォルトで末尾に改行が入るが、end= で文字列を指定することで末尾を変更できる
print('Hello', end=",")
print('World')

print('Hello', end="")
print('World')

# / で割り算
print(1 / 5)
print(1.0 / 5.0)

# //で割り算⇒切り捨てて除算
print(5 // 2)
print(1.7 // 0.6)
print(3.14 // 1)

# べき乗⇒2,3乗など同じ数をかけるもの
print(5 ** 2)
print(10 ** 2)

# 文字列のインデックスiの文字を取得する
# 文字カウントは0から始まる
s = "Hello, World!"
print(s[0])

# 文字列後ろから数える時
print(s[-1])
print(s[-2])

# 文字列のインデックスがi～j-1の部分取得
a = "Hello, World!"
# インデックス1～3までを取得
print(a[1:4])
# インデックス0～4までを取得
print(a[:5])
# インデックス7以降を取得
print(a[7:])