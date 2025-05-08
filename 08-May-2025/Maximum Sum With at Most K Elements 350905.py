# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        R = len(grid)
        C = len(grid[0])
        for i in range(R):
            row = grid[i]
            temp = []
            for num in row:
                heappush(temp, -num)
            for _ in range(limits[i]):
                heappush(heap, heappop(temp))
        res = 0
        for _ in range(k):
            res += -heappop(heap)
        return res