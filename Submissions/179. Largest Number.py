class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        nums = [str(num) for num in nums]

        # Custom sort based on concatenated string representations
        nums.sort(key=lambda x: x*10, reverse=True)

        # Handle case where all numbers are 0
        if nums[0] == '0':
            return '0'

        # Concatenate sorted strings and return
        return ''.join(nums)
        