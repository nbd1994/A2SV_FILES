# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def get_pos(s):
            r = N - 1 - (s - 1) // N
            c = (s - 1) % N
            if (N - 1 - r) % 2 == 1:
                c = N - 1 - c
            return r, c

        visited = set()
        queue = deque([1])
        moves = 0
        while queue:
            for i in range(len(queue)):
                s = queue.popleft()
                for i in range(1, 7):
                    next_s = s + i
                    if next_s > N * N:
                        continue
                    r, c = get_pos(next_s)
                    if board[r][c] != -1:
                        next_s = board[r][c]
                    if next_s == N * N:
                        return moves + 1
                    if next_s not in visited:
                        visited.add(next_s)
                        queue.append(next_s)
            moves += 1
        return -1
