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

# リストに対してメソッドを実行
team = ["勇者", "戦士", "魔法使い", "忍者"]
# この下に、インデックス3に「盗賊」を追加して、リストを表示する処理を記述する
team.insert(3, "盗賊")

print(team)

# 継承
class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")


class JewelryBox(Box):
    def look(self):
        print("宝箱はキラキラと輝いている。")


box = Box("鋼鉄の剣")
box.open()

jewelrybox = JewelryBox("魔法の指輪")
jewelrybox.look()
jewelrybox.open()

# メソッドのオーバーライド
class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")


class MagicBox(Box):
    def look(self):
        print("宝箱は妖しく輝いている。")

    def open(self):
        print("宝箱を開いた。" + self.item + "が襲ってきた！")


box = Box("鋼鉄の剣")
box.open()

magicbox = MagicBox("モノマネモンスター")
magicbox.look()
magicbox.open()

# a~zまでを表示
for i in range(97, 97 + 26):
    print(chr(i))