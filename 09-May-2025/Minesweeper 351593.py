# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        que = deque([tuple(click)])
        R = len(board)
        C = len(board[0])
        visited = set([tuple(click)])
        def inbound(i,j):
            return 0 <= i < R and 0 <= j < C
        while que:
            for _ in range(len(que)):
                r,c = que.popleft()
                if board[r][c] == 'E':
                    mine_count = 0
                    for x,y in directions:
                        dx,dy = r+x, c+y
                        if inbound(dx,dy):
                            if board[dx][dy] == 'M':
                                mine_count += 1
                    if mine_count > 0:
                        board[r][c] = str(mine_count)
                    else:
                        board[r][c] = 'B'
                        for x,y in directions:
                            dx,dy = r+x, c+y
                            if inbound(dx,dy) and (dx,dy) not in visited:
                                visited.add((dx,dy))
                                que.append((dx,dy))
        return board