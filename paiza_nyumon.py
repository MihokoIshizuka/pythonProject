# HTMLで出力する方法
print("<p>ハロー、パイザ</p>")

# 0～1の間でランダムな数値を出力する
import random
number = random.random()
print(str(number) + "匹のこぶた")
# 指定した範囲でランダムな数値を出力する
number = random.randint(1,100)
print(str(number) + "匹のこぶた")

# ランダムなサイコロの値を出力
x = random.randint(1,6)
print("サイコロの目は" + str(x) + "です")

# if文
number = random.randint(1, 3)
print("あなたの順位は" + str(number) + "位です")
if number == 1:
    print("おめでとう")