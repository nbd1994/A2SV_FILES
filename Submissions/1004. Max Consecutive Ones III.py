class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        zcount = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zcount+=1
            while zcount>k:
                if nums[left]==0:
                    zcount-=1
                left+=1
            ans = max(ans, right-left+1)
    
        return ans