class Solution:
    def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        left = 0
        mp = {
            "T": 0,
            "F": 0
        }
        maxcount = 0
        maxconsc = 0
        for right in range(len(ak)):
            mp[ak[right]]+=1
            maxcount = max(maxcount, mp[ak[right]])
            while right-left+1 > maxcount+k:
                mp[ak[left]]-=1
                left+=1
            maxconsc = max(maxconsc, right-left+1)
        return maxconsc