class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right]==0 and k == 1:
                k=0
                # ans = max(ans, right-left+1)
            elif nums[right]==0:
                while nums[left]==1:
                    left+=1
                left+=1
            ans = max(ans, right-left+1)
    
        return ans-1