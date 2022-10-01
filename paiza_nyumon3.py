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


# 可変長引数
def introduce(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者", "村人", "兵士")


# 可変長引数-辞書
def introduce(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)

introduce(hero="初めまして", villager="こんにちは", solder="よろしくお願いします")

# キーワード引数
def introduce(name = "私は", role = "村人"):
    print(name + role + "です")
introduce()
# 初期値でない値を入れる
introduce(role = "戦士")

# クラスを作成する
class Player:
    def walk(self):
        print("勇者は荒野を歩いていた")
    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

player1 = Player()
player1.walk()
player1.attack("スライム")


# 変数をクラスで管理する
class Player:
    def __init__(self, job):
        self.job = job

    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()


# RPGの敵クラスを作る
class Enemy:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print(self.name + "は勇者を攻撃した")

enemies = []

enemies.append(Enemy("スライム"))
enemies.append(Enemy("ドラゴン"))
enemies.append(Enemy("モンスター"))

for enemy in enemies:
    enemy.attack()


# クラスで、引数と戻り値のあるメソッドを作る
class Item:
    tax = 1.08

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return int(self.price * self.quantity * Item.tax)

apple = Item(120, 15)
total = apple.total()
print("合計金額は" + str(total) + "円です")

orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")