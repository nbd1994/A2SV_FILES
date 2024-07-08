class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = pre
            pre*=nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i]*=post
            post*=nums[i]
        return ans