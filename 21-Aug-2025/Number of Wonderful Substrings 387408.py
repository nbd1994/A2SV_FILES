# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        mask = 0
        count[0] = 1
        res = 0
        for ch in word:
            bit = ord(ch) - ord('a')
            mask = mask ^ (1 << bit)

            res += count[mask]
            for i in range(10):
                res += count[mask ^ (1 << i)]
            count[mask] += 1
        return res