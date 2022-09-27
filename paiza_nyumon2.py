# 辞書
enemyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemyDictionary)
print(enemyDictionary["ザコ"])

level = "ザコ"
print(enemyDictionary[level])

# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(len(enemies))
# 要素の追加
enemies["ザコ2"] = "メタルモンスター"
print(enemies)
print(len(enemies))
#要素の上書き
enemies["中ボス"] = "レッドドラゴン"
print(enemies)
print(len(enemies))
# 要素の削除
del enemies["ザコ"]
print(enemies)
print(len(enemies))

# 辞書のループ処理
for rank in enemies :
    print(rank + "があらわれた！")
for (rank, enemy) in enemies.items():
    print(rank + "の" + enemy + "があらわれた！")

# ループ処理で点数の合計を計算
points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
for (key,point) in points.items():
    sum += point
print(sum)

# 辞書の整列
weapons = {"イージスソード":40, "ウィンドスピア":12, "アースブレイカー":99}
print(sorted(weapons.items()))
print(sorted(weapons))

# アイテムリストの作成
# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}
# アイテムを入力する個数を決めて入力
num = int(input())
li =[]
# アイテムの個数分リストの要素を作成
for i in range(num):
    li.append(input())
# リストのアイテムを一つずつ画像に変換
for item_name in li:
    print("<img src='" + items_imges[item_name] + "'>")