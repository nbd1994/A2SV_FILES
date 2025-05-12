# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
    n, k = map(int, sys.stdin.readline().split())
    u =  n - 1
    if k >= u:
        print(1)
    else:
        print(n)
