# リストを作成する
li = [1, 2, 3]
print(li)

# 型の異なるリストを繋げる
a = [1, 2, 3]
b = ["apple", "banana", "cat"]
c = [a, b]
print(c)

# リストのインデックスを取得する
li = [5, 3, 8]
print(li[0])
print(li[-1])

# リストの長さを取得
print(len(li))

# リストを統合させる
a = [1, 2, 3, 4 ,5]
b = [6, 7, 8, 9, 10]
print(a + b)

# リストの末尾に要素を追加するappendメソッド
li = [2, 4, 6, 8]
li.append(10)
print(li)

# リストの末尾の要素を削除するpopメソッド
li = [1, 2, 3, 4]
a = li.pop()
print(a)
print(f"長さ：{len(li)}, 要素：{li}")

