# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

n, b = list(map(int, input().split()))
attacks = list(map(int, input().split()))

bases = []
for _ in range(b):
    bases.append(list(map(int, input().split())))

bases.sort()
pfx = [[] for _ in range(b)]
defence = [0 for _ in range(b)]
pfx[0] = bases[0][1]
defence[0] = bases[0][0]
for i in range(1,b):
    pfx[i] = pfx[i-1] + bases[i][1]
    defence[i] = bases[i][0]
def func(attack):
    left = 0
    right = len(defence)-1
    while left <= right:
        mid = (left+right)//2
        defence_ = defence[mid]
        if defence_ <= attack:
            left =mid+ 1
        else:
            right = mid- 1
    return pfx[right] if right >= 0 else 0

res = [0]*n

for j in range(n):
    res[j] = func(attacks[j])
print(*res)
