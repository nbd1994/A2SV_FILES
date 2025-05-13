# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

#main intuition: we should cut between numbers that have the biggest gaps
import sys
n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

gaps = [nums[i+1] - nums[i] for i in range(n-1)]
gaps.sort(reverse=True)

total_cost = nums[n-1] - nums[0]
reduced_cost = sum(gaps[:k-1])
print(total_cost - reduced_cost)