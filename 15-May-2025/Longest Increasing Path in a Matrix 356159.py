# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        answer = 1
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        dp = [[0]*COLS for _ in range(ROWS)]
        def inbound(a,b):
            return 0<=a<ROWS and 0<=b<COLS
        def dfs(r,c):
            if not inbound(r,c):
                return 0
            res = 1
            if dp[r][c] > 0:
                return dp[r][c]
            for x,y in directions:
                dx,dy = r+x, c+y
                if inbound(dx,dy) and matrix[dx][dy] > matrix[r][c]:
                    res = max(res, 1 + dfs(dx,dy))
            dp[r][c] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                answer = max(answer, dfs(i,j))
        return answer