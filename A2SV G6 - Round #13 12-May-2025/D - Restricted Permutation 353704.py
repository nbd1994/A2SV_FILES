# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

import sys
from heapq import *
n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n)]
indegree = [0]*n
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a = a-1
    b = b-1
    adj_list[a].append(b)
    indegree[b] += 1
heap = []
for i in range(n):
    if indegree[i] == 0:
        heappush(heap, i)
res = []
while heap:
    # temp = []
    for _ in range(len(heap)):
        val = heappop(heap)
        res.append(val + 1)
        for neig in adj_list[val]:
            indegree[neig] -= 1
            if indegree[neig] == 0:
                heappush(heap, neig)
print(*res) if len(res)==n else print(-1)