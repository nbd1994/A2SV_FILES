# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(start, end):
            prev, cur = None, start
            while cur != end:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        cnt , temp = 0, head
        while temp and cnt< k:
            temp = temp.next
            cnt += 1
        if cnt < k:
            return head
        new_head = reverseList(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head 