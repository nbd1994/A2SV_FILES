# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

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
    visited = [0]*(n+1)
    # visited = set()
    visited[k] = 1
    dist_node = 0
    distance = 0
    while que:
        for _ in range(len(que)):
            dist_node = node = que.popleft()
            for neig in adj_list[node]:
                if not visited[neig]:
                    que.append(neig)
                    visited[neig] = 1
        distance += 1
    return (dist_node, distance-1)
first_dist_node = bfs1(1)[0]
diameter = bfs1(first_dist_node)[1]
print(diameter * 3)