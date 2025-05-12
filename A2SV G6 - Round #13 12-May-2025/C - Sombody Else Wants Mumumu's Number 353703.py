# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

from collections import Counter
import sys
from heapq import *
tests = int(sys.stdin.readline())
for _ in range(tests):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    res = 0
    cnt = Counter(nums).items()
    nums_count = []
    for k,v in cnt:
        heappush(nums_count, (-v, k))

    # print(nums_count)
    while len(nums_count) >= 2:
        v1, k1 = heappop(nums_count)
        v2, k2 = heappop(nums_count)
        # print(v1,v2)
        if v1+1 != 0:
            heappush(nums_count, (v1+1, k1))
        if v2+1 != 0:
            heappush(nums_count, (v2+1, k2))
    
    for v, k in nums_count:
        res += (-v)
    print(res)
