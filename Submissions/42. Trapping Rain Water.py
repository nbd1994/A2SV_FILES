class Solution:
    def trap(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for r , right in enumerate(heights):
            while stack and heights[stack[-1]] < right:
                bar = heights[stack.pop()]
                if stack:
                    l = stack[-1]
                    left = heights[stack[-1]]
                    min_ = min(left, right)
                    res +=(r-l-1) * (min_ - bar)
            stack.append(r)
        return res