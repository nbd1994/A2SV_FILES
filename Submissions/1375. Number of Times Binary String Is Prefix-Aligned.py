class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt = 0
        ff = [0]*len(flips)
        l = 0
        for i in range(len(flips)):
            ff[flips[i]-1] = 1
            while l < len(flips) and ff[l]==1:
                l+=1
            if l == i+1:
                cnt+=1
        return cnt