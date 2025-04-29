# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for _list in lists:
            curr = _list
            while curr:
                heapq.heappush(heap,curr.val)
                curr = curr.next
        curr = ListNode()
        dummy = curr
        while heap:
            num = heapq.heappop(heap)
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
