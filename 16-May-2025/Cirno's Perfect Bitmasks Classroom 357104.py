# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
    n = int(sys.stdin.readline())
    if n == 1:
        print(3)
    elif n & (n-1) == 0:
        print(n+1)
    else:
        for i in range(32):
            if n & (1 << i):
                print(1 << i)
                break