class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        ans = []
        for num in nums:
            summ+=num
            ans.append(summ)
        return ans
        