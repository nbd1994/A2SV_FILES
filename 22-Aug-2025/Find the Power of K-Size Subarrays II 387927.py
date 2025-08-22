# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0

        consec_count = 1
        for right in range(len(nums)):
            if right > 0 and nums[right - 1] + 1 == nums[right]:
                consec_count += 1
            
            if right - left + 1 > k:
                if nums[left] + 1 == nums[left+1]:
                    consec_count -= 1
                left += 1
            if right - left + 1 == k:
                if consec_count == k:
                    res.append(nums[right])
                else:
                    res.append(-1)
        return res