# 繰り返し処理 for in
    # カウンタ変数はiやjが多い
for i in range(10):
    print("hello paiza:" + str(i))
    # 指定された範囲で出力6~10
for i in range(6, 11):
    print("hello" + str(i))
for i in range(1, 13):
    print(str(i) + "月")

# whileによるループ処理
i = 0
while i <= 5:
    print(i)
    # カウンタ変数の更新が必須！
    i += 1

# スライムを倒すプログラム
import random
hp = 30
while hp > 0:
    hit = random.randint(1, 10)
    print("スライムに" +str(hit) + "のダメージを与えた");
    hp -= hit
print("スライムを倒した")

# 偶数の出力プログラム
i = 1
while i <= 10:
    if (i % 2 == 0):
        print(i)
    i += 1

# HTMLで年齢のセレクトボックス
print("<select name=\'age\'>")
# rangeの場合は0~9歳が選択される
for age in range(10):
    # +1することでageの範囲が1~10歳にずれる
    print("<option>" + str(age + 1) + "歳</option>")
print("</select>")

# 標準入力とfor文の組み合わせ
num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    print(i)
    i += 1