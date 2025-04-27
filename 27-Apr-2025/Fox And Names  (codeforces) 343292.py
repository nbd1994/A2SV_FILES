# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import deque
import sys
n = int(sys.stdin.readline())
indegree = [0]*26
adj_list = [[] for _ in range(26)]
names = []
def idx(ch):
    return ord(ch) - ord('a')
for _ in range(n):
    string = input()
    names.append(string)
a,b = 0,1
impossible = False
while b < len(names):
    name1 = names[a]
    name2 = names[b]
    min_length = min(len(name1), len(name2))
    found = False
    for i in range(min_length):
        if name1[i] != name2[i]:
            found = True
            adj_list[idx(name1[i])].append(idx(name2[i]))
            indegree[idx(name2[i])] += 1
            break
    if not found and len(name1) > len(name2):
        impossible = True
        break
    a += 1
    b += 1
topo_order = []
if not impossible:
    # print(adj_list)
    que = deque()
    for letter in range(26):
        if indegree[letter] == 0:
            que.append(letter)
    while que:
        for _ in range(len(que)):
            letter = que.popleft()
            topo_order.append(chr(letter + ord('a')) )
            for neig in adj_list[letter]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    que.append(neig)
    if len(topo_order) != 26:
        impossible = True
        
if not impossible:
    print(''.join(topo_order))
else:
    print('Impossible')