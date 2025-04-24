# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        que = deque([(sr,sc)])
        starting_color = image[sr][sc]
        visited = set([(sr,sc)])
        image[sr][sc] = color
        def in_bound(a,b):
            return 0 <= a < ROWS and 0 <= b < COLS
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        while que:
            x,y = que.popleft()
            for a,b in directions:
                dx, dy = x+a, y+b
                if in_bound(dx,dy) and (dx,dy) not in visited and image[dx][dy] == starting_color:
                    image[dx][dy] = color
                    que.append((dx,dy))
                    visited.add((dx,dy))
        return image
        