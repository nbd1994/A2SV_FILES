# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using quick select
        #since we're looking for the kth largest we have to create a decreasing array
        # def partition(left, right):
        #     piv_idx = random.randint(left,right)
        #     pivot = nums[piv_idx]
        #     nums[left],nums[piv_idx] = nums[piv_idx], nums[left]
        #     w = left + 1
        #     for r in range(left+1, right+1):
        #         if nums[r] > pivot: #we bring the larger elements to the left
        #             nums[r],nums[w] = nums[w], nums[r]
        #             w += 1
        #     nums[left], nums[w-1] = nums[w-1], nums[left]
        #     return w-1
        # def quick_select(left, right):
        #     if left <= right:
        #         pivot_index = partition(left,right)
        #         if pivot_index < k-1:
        #             return quick_select(pivot_index+1, right)
        #         elif pivot_index > k-1:
        #             return quick_select(left, pivot_index-1)
        #         else:
        #             return nums[k-1]
        # return quick_select(0, len(nums)-1)

        #using heap
        negative_nums = []
        for num in nums:
            heapq.heappush(negative_nums, -num)
        res = 0
        while k > 0:
            res = - heapq.heappop(negative_nums)
            k -= 1
        return res
