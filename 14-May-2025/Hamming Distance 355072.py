# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        cnt = 0
        for i in range(32):
            if a & (1 << i):
                cnt += 1
        return cnt