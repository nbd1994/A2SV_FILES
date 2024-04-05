class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i], nums[i+1] = nums[i]*2, 0
                i+=1
            i+=1
        z = 0
        z = nums.count(0)
        nums = [num for num in nums if num!=0]
        return nums + ([0]*z)
        