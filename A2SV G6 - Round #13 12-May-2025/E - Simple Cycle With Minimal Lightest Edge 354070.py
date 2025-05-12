# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

import bisect
from collections import deque
import sys
n = int(sys.stdin.readline())
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def bfs1(k):
    que = deque([k])
    visited = set()
    visited.add(k)
    dist_node = 0
    while que:
        for _ in range(len(que)):
            dist_node = node = que.popleft()
            for neig in adj_list[node]:
                if neig not in visited:
                    que.append(neig)
                    visited.add(neig)
    return dist_node

first_distant_node = bfs1(1)
second_distant_node = bfs1(first_distant_node)

max_dist = [0]*(n+1)
def bfs2(k, max_d):
    visited = set()
    visited.add(k)
    distance_from_k = 1
    que = deque([k])
    while que:
        for _ in range(len(que)):
            node = que.popleft()
            for neig in adj_list[node]:
                if neig not in visited:
                    que.append(neig)
                    visited.add(neig)
                    max_d[neig] = max(max_d[neig], distance_from_k)
        distance_from_k += 1
bfs2(first_distant_node, max_dist)
bfs2(second_distant_node, max_dist)

max_dist.sort()
ans = []
for i in range(n+1):
    x = bisect.bisect_left(max_dist, i)
    x = x-1
    if i > 0:
        grouped = n -x
        ans.append(min(n, n-grouped + 1))
print(*ans)