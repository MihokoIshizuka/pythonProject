# 関数を作る
def say_hello():
    print("hello python")
say_hello()


# 引数と戻り値を追加する
def sum(x, y):
    return x + y
num1 = sum(3, 4)
print(num1)

# RPGの攻撃シーン
import random

def attack(enemy):
    print("勇者は" + enemy + "を攻撃した")
    hit = random.randint(1, 10)
    if hit < 6:
        print(enemy + "に" + str(hit) + "のダメージを与えた！")
    else:
        print("クリティカルヒット！" + enemy + "に、100のダメージを与えた！")

enemies = ["スライム", "モンスター", "ドラゴン"]
for enemy in enemies:
    attack(enemy)