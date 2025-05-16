# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
def count_good_segments(n, k, a):
    max_q = deque()
    min_q = deque()
    left = 0
    result = 0

    for right in range(n):
        # Maintain max deque
        while max_q and a[right] > max_q[-1]:
            max_q.pop()
        max_q.append(a[right])

        # Maintain min deque
        while min_q and a[right] < min_q[-1]:
            min_q.pop()
        min_q.append(a[right])

        # Shrink window if spread is too big
        while max_q[0] - min_q[0] > k:
            if max_q[0] == a[left]:
                max_q.popleft()
            if min_q[0] == a[left]:
                min_q.popleft()
            left += 1

        # All subarrays ending at 'right' and starting from left to right are valid
        result += (right - left + 1)

    return result
n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(count_good_segments(n,k,nums))




# res = 0
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         x = sorted(nums[i:j+1])
#         cur_max = x[-1]
#         cur_min = x[0]
#         if cur_max - cur_min <= k:
#             res += 1
# print(res)