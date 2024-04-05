class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0 and nums[j]==0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[j]!=0:
                j+=1
