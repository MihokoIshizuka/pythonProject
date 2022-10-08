# 複数の整数を半角スペース区切りでリストに格納する
a = []
a = [int(x) for x in input().split()]
for ans in a:
    print(ans)

# 2 行目で与えられる N 個の整数の入力
n = int(input())
N = [n]
N = [int(x) for x in input().split()]
for ans in N:
    print(ans)

# バスの運賃
n, m = (int(x) for x in input().split())
point = 0
for i in range(m):
    price = int(input())
    if point >= price:
        point -= price
        print(n, end =" ")
        print(point)
    else:
        n -= price
        point += price // 10
        print(n, end = " ")
        print(point)