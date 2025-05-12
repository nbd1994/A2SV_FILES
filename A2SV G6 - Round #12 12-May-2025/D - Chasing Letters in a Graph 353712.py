# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

## using dfs
# import sys
# n, m = list(map(int, sys.stdin.readline().split()))
# letters = input()
# adj_list = [[] for _ in range(n)]
# for _ in range(m):
#     a,b = list(map(int, sys.stdin.readline().split()))
#     adj_list[a-1].append(b-1)
# # print(adj_list)
# VISITED = 2
# VISITING = 1
# UNVISITED = 0

# visited = [UNVISITED for _ in range(n)]
# values = [[0]*26 for _ in range(n)]

# def dfs(node):
#     if visited[node] == VISITED:
#         return False
#     if visited[node] == VISITING:
#         return True
    
#     visited[node] = VISITING
#     for neig in adj_list[node]:
#         is_cyc = dfs(neig)
#         if is_cyc:
#             return True
    
#     for neig in adj_list[node]:
#         for letter in range(26):
#             values[node][letter] = max(values[node][letter], values[neig][letter])
#     cur_letter = ord(letters[node]) - ord('a')
#     values[node][cur_letter] += 1

#     visited[node] = VISITED
#     return False 

# res = 0
# for node in range(n):
#     if visited[node] == UNVISITED:
#         is_cycle = dfs(node)
#         if is_cycle:
#             res = -1
#             break
# if res != -1:
#     for node in range(n):
#         for letter in range(26):
#             res = max(res, values[node][letter])
# print(res)


## using bfs
from collections import deque
import sys
n, m = list(map(int, sys.stdin.readline().split()))
adj_list = [[] for _ in range(n)]
indegree = [0]*n
letters = input()
for _ in range(m):
    a,b = list(map(int, sys.stdin.readline().split()))
    adj_list[b-1].append(a-1)
    indegree[a-1] += 1

values = [[0]*26 for _ in range(n)]
que = deque()
visited = set()
for node in range(n):
    if indegree[node] == 0:
        que.append(node)
        visited.add(node)
res = -1
while que:
    for _ in range(len(que)):
        node = que.popleft()
        cur_letter = ord(letters[node]) - ord('a')
        values[node][cur_letter] += 1
        for neig in adj_list[node]:
            for letter in range(26):
                values[neig][letter] = max(values[neig][letter], values[node][letter])
            indegree[neig] -= 1
            if indegree[neig] == 0:
                que.append(neig)
                visited.add(neig)
if len(visited) == n:
    for node in range(n):
        for letter in range(26):
            res = max(res, values[node][letter])
print(res)