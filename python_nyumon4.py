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