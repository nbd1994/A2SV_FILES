# Problem: A - Two Ranges - https://codeforces.com/gym/604781/problem/A

import sys

q = int(sys.stdin.readline())
for _ in range(q):
    l1, r1, l2, r2 = list(map(int, sys.stdin.readline().split()))

    first_num = l1
    second_num = l2 if l2 != l1 else r2
    print(first_num, second_num)
