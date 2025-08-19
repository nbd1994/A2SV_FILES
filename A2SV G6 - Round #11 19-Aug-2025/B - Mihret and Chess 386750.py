# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

from cmath import sqrt
from math import ceil, floor
import sys
r1,c1,r2,c2 = map(int, sys.stdin.readline().split())

rook = 2
king = 0
bishop = 0

if r1 == r2 or c1 == c2:
    rook = 1


if (r1+c1)%2 == (r2+c2)%2:
    if r1-c1 == r2-c2 or r1+c1 == r2+c2:
        bishop = 1
    else:
        bishop = 2

king = max(abs(r1-r2), abs(c1-c2))
print(rook, bishop, king)