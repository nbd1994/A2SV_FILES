# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in range(32):
            if (left >> i) & 1: # if right most bit is one
                rem = left % (1 << (i+1))
                diff = (1 << (i+1)) - rem
                if right - left < diff:
                    res = res | (1 << i)
        return res

