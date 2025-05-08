# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(1,n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heappush(heap, diff)
            if len(heap) > ladders:
                val = heappop(heap)
                bricks -= val
                if bricks < 0:
                    return i - 1
        return n-1