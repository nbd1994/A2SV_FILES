# Problem: E - Direct Without Regret - https://codeforces.com/gym/606404/problem/E

from collections import deque
import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
    
    n, m = list(map(int, sys.stdin.readline().split()))

    directed_edges = []
    undirected_edges = []

    indegree = [0]*n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        t, a, b = list(map(int, sys.stdin.readline().split()))
        if t == 1:
            adj_list[a-1].append(b-1)
            indegree[b-1]+=1
            directed_edges.append((a,b))
        else:
            undirected_edges.append((a-1, b-1))

    que = deque()
    top_order = []
    for node in range(n):
        if indegree[node] == 0:
            que.append(node)

    while que:
        for _ in range(len(que)):
            node = que.popleft()
            top_order.append(node)
            for neig in adj_list[node]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    que.append(neig)
    if len(top_order) != n:
        print('NO')
    else:
        print('YES')
        order = [0]*n
        for idx, node in enumerate(top_order):
            order[node] = idx
        
        for a,b in directed_edges:
            print(a,b)
        for a,b in undirected_edges:
            if order[a] < order[b]:
                print(a+1, b+1)
            else:
                print(b+1, a+1)