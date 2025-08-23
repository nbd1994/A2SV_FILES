# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

from collections import defaultdict
from types import GeneratorType
import sys, threading

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

mp = defaultdict(int)
visited = set()

def on_edge(a, b):
    return a == 0 or a == n - 1 or b == 0 or b == m - 1

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def inbound(a, b):
    return 0 <= a < n and 0 <= b < m

@bootstrap
def dfs0(i, j):
    if inbound(i, j) and (i, j) not in visited and grid[i][j] == '.':
        visited.add((i, j))
        for x, y in directions:
            yield dfs0(i + x, j + y)
    yield

@bootstrap
def dfs(r, c):
    if inbound(r, c) and (r, c) not in visited and grid[r][c] == '.':
        visited.add((r, c))
        temp = 1
        for x, y in directions:
            temp += yield dfs(r + x, c + y)
        yield temp
    else:
        yield 0

for i in range(n):
    for j in range(m):
        if (i, j) not in visited and grid[i][j] == '.' and on_edge(i, j):
            dfs0(i, j)

for i in range(n):
    for j in range(m):
        if (i, j) not in visited and grid[i][j] == '.' and not on_edge(i, j):
            count = dfs(i, j)
            mp[(i, j)] = count

visited = set()

@bootstrap
def second_dfs(r, c):
    if inbound(r, c) and (r, c) not in visited and grid[r][c] == '.' and not on_edge(r, c):
        visited.add((r, c))
        grid[r][c] = '*'
        for x, y in directions:
            yield second_dfs(r + x, c + y)
    yield

small_lakes = sorted(mp.items(), key=lambda x: x[1])
no_of_lakes = len(small_lakes)

res = 0
for cell, c in small_lakes[:no_of_lakes - k]:
    i, j = cell
    res += c
    second_dfs(i, j)

print(res)
for i in range(n):
    print("".join(grid[i]))
