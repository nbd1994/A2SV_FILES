# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

from math import ceil

tests = int(input())
for _ in range(tests):
    n, s = list(map(int, input().split()))
    min_num = 0
    max_num = s
    pos = n//2+1
    print(max_num // pos)

    # def calculate_sum(med):
    #     right_sum = med * pos
    #     return right_sum

    # while min_num <= max_num:
    #     mid = min_num + (max_num - min_num)//2
    #     summ = calculate_sum(mid)
    #     if summ <= s:
    #         min_num = mid + 1
    #     else:
    #         max_num = mid - 1
    # print(max_num)
