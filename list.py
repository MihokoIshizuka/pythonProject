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

# リストの要素を指定して削除するremoveメソッド
li = [5, 3, 4, 3, 2]
# 最初に現れる3の要素を削除する
li.remove(3)
print(li)

# リストのインデックスiの要素を削除するdelメソッド
li = ["apple", "banana", "cat"]
# i=1の要素を削除
del li[1]
print(f"長さ： {len(li)}, 要素： {li}")
# 指定された範囲i～j-1の要素を削除(1~2)
del li[1:3]
print(f"長さ： {len(li)}, 要素： {li}")

# リストの要素をソート
a = [1, 3, 2]
# 要素を昇順に並び替える
a.sort()
print(a)
# リストの要素を破壊的に、降順に並び替える
a.sort(reverse=True)
print(a)

b = ["apple", "cat", "banana"]
# 要素をアルファベット昇順に並び替える
b.sort()
print(b)
# 要素を破壊的に、降順に並び替える
b.sort(reverse=True)
print(b)
# ソートすることで要素のインデックスは変わる
print(b[0])

# 非破壊的にソートすることでリストの要素そのものの順番は変わらないsortedメソッド
a = [1, 4, 3, 2, 6, 5]
print(sorted(a))
print(a)
print(sorted(a, reverse=True))
print(a)

# リストから文字列へ変更（リスト内の要素は文字列型にすること）
li = ["A", "B", "C"]
# 半角スペースを区切り文字として結合
print(" ".join(li))
# 空文字列を区切り文字として結合
print("".join(li))
# /を区切りとして文字列を結合
print("/".join(li))

# 文字列からリストへ変更
s = "paiza"
print(list(s))
# , 区切りでリスト化するsplit
n = "apple,banana,cat"
print(n.split(","))

# リストを要素として出力
team = ["勇者", "戦士", "魔法使い"]
for i in team:
    print(i)

# 複数行のカンマ区切りデータを出力する
import sys
for line in sys.stdin.readlines():
    enemy = line.rstrip().split(",")
    print(enemy[0] + "が" + enemy[1] + "匹現れた")

# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王
import random
line = input().rstrip().split(",")
for enemy in line:
    print(enemy + "が現れた！")

num = len(line)
print("敵は" + str(num) + "匹")

attack = random.randrange(num)
print(line[attack] + "に会心の一撃！" + line[attack] + "を倒した！")