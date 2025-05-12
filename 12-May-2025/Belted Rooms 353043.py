# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
    n = int(sys.stdin.readline())
    directions = input()
    set_ = set(directions)
    res = 0
    for i in range(n):
        next_ = directions[i]
        prev = directions[i-1]
        if next_ == '>' and '<' not in set_:
            res += 1
        elif next_ == '<' and '>' not in set_:
            res += 1
        elif next_ == '-' or prev == '-':
            res += 1
    print(res)
