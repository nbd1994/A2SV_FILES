# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            else:
                # choose to include nums[i] in the subset
                subset.append(nums[i])
                backtrack(i+1)

                # now do it without nums[i]
                subset.pop()
                backtrack(i+1)
        backtrack(0)
        return res
        

        