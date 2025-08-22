# Problem: D - Merbebt and Maze - https://codeforces.com/gym/604781/problem/D

from collections import defaultdict, deque
test_cases = int(input())
for _ in range(test_cases):
    input()
    n, k = map(int, input().split())
    frie_pos = list(map(int, input().split()))
    adj = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    #first mark the positons of friends
    dist_frie = [float('inf')] * (n+1)
    queue = deque()
    for pos in frie_pos:
        dist_frie[pos] = 0
        queue.append(pos)
    
    #bfs from the friends to calculate the minimum distance to reach each node
    while queue:
        vertex = queue.popleft()
        for neigh in adj[vertex]:
            if dist_frie[neigh] > dist_frie[vertex] + 1: #this is the minimum distance to reach this node starting from one of the friends position
                dist_frie[neigh] = dist_frie[vertex] + 1 #this means min(dist_frie[neigh],dist_frie[vertex]+1)
                queue.append(neigh)
    
    #bfs from merbebt to reach the nearest leaf node
    queue.append((1,0)) #node, distance from merbebt pos to each node
    visited = set([1])
    # print(queue)
    while queue:
        vertex, dist = queue.popleft()
        if vertex != 1 and len(adj[vertex]) == 1:#it reaches the leafnode and it should not be the start node 
            print('YES')
            break
        for neigh in adj[vertex]:
            if neigh not in visited and dist + 1 < dist_frie[neigh]:#to check if merbebt is closer than her friends to reach the node
                queue.append((neigh,dist+1))
                visited.add(neigh)
            
    else:
        print('NO')
