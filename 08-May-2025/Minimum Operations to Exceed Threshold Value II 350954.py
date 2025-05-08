# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while len(nums) >= 2:
            n1 = heappop(nums)
            n2 = heappop(nums)
            if n1 >= k:
                break
            heappush(nums, min(n1,n2)*2 + max(n1,n2))
            operations += 1
        return operations