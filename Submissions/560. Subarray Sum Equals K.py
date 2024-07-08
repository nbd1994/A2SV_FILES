class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0 : 1}
        ans = 0
        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            ans += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return ans