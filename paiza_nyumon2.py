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