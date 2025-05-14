# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

import sys
n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))
prefix_cost = cost.copy()
for i in range(1, n): prefix_cost[i]+=prefix_cost[i-1]

cost_sorted = sorted(cost)
prefix_cost_sorted = cost_sorted
for i in range(1, n): prefix_cost_sorted[i]+=prefix_cost_sorted[i-1]
m = int(sys.stdin.readline())
for _ in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 1:
        if l == 1:
            print(prefix_cost[r-1])
        else:
            print(prefix_cost[r-1] - prefix_cost[l-2])
    else:
        if l == 1:
            print(prefix_cost_sorted[r-1])
        else:
            print(prefix_cost_sorted[r-1] - prefix_cost_sorted[l-2])
