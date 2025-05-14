# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xor_prefix = arr
        for i in range(1, n):
            xor_prefix[i] = xor_prefix[i] ^ xor_prefix[i-1]
        res = []
        for l,r in queries:
            if l == 0:
                res.append(xor_prefix[r])
            else:
                res.append(xor_prefix[r] ^ xor_prefix[l-1])
        return res
