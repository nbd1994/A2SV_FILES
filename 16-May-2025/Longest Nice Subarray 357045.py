# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        state = [0]*32
        res = 0
        left = 0
        n = len(nums)
        for right in range(n):
            for i in range(32):
                if nums[right] & (1 << i):
                    state[i] += 1
            while left < n and  max(state) > 1:
                for j in range(32):
                    if nums[left] & (1 << j):
                        state[j] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res