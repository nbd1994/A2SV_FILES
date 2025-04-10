# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        num_set = []
        for num in nums:
            if num not in mp: num_set.append(num)
            mp[num] = mp.get(num,0)+1
        def partition(left, right):
            piv_idx = left
            pivot = mp[num_set[left]]
            w = left + 1
            for r in range(left+1, right+1):
                if mp[num_set[r]] > pivot:
                    num_set[w],num_set[r] = num_set[r], num_set[w]
                    w += 1
            num_set[left], num_set[w-1] = num_set[w-1], num_set[left]
            return w - 1
        def quick_select(l, r):
            pivot_index = partition(l, r)
            if pivot_index == k - 1:
                return num_set[:k]
            elif pivot_index < k - 1:
                return quick_select(pivot_index+1, r)
            else:
                return quick_select(l, pivot_index-1)
        return quick_select(0, len(num_set)-1)
