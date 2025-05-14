# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    r = int(input())
    reds = list(map(int ,input().split()))
    b = int(input())
    blues = list(map(int, input().split()))

    red_max, red_sum, blu_max, blu_sum = 0, 0, 0, 0
    for i in range(r):
        red_sum += reds[i]
        red_max = max(red_max, red_sum)
    for j in range(b):
        blu_sum += blues[j]
        blu_max = max(blu_max, blu_sum)
    print(red_max + blu_max)