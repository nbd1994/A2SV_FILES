class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            flag = False
            isIn = any(num in range(r[0], r[len(r)-1]+1) for r in ranges)
            if not isIn:
                return False
        return True

