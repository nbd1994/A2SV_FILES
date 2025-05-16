# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

from collections import defaultdict
import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    state = [0]*32
    for num in nums:
        for i in range(32):
            if num & (1 << i):
                state[i] += 1

    min_cnt = n

    for k in state:
        if k != 0 and k < min_cnt:
            min_cnt = k
    res = []
    for i in range(1, min_cnt + 1):
        if all(nm % i == 0 for nm in state if nm != 0):
            res.append(i)
    print(*res)
