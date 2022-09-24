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

# おみくじ
x = random.randint(1,100)
if x % 2 == 0 and x % 3 == 0:
    print("大吉")
elif x % 2 == 0:
    print("中吉")
elif x % 3 == 0:
    print("小吉")
else:
    print("吉")

# if文
number = random.randint(1, 5)
print("あなたの順位は" + str(number) + "位です")
if number == 1:
    print("おめでとう")
elif number == 2:
    print("あと少し")
else:
    print("よくがんばったね")

# 西暦年を昭和年に変換
seireki = random.randint(1926, 1988) #西暦年
print("西暦" + str(seireki) + "年は", end = "")
showa = seireki - 1925
print("昭和" + str(showa) + "年です")

# 平成を令和に変換
ad_year = random.randint(2019, 2099) #西暦年
print("西暦" + str(ad_year) + "年は", end = "")
era_year = ad_year - 2018
print("令和" + str(era_year) + "年です")