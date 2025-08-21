# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones_count = bin(num2).count('1')
        x = 0

        for i in range(31, -1, -1):
            if ones_count == 0:
                break
            if(num1 & (1 << i)):
                x |= (1 << i)
                ones_count -= 1
        for i in range(32):
            if ones_count == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                ones_count -= 1
        return x