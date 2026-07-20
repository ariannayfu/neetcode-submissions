# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def twoPoint(slow: Optional[ListNode], fast: Optional[ListNode]) -> bool:
            if not fast or not fast.next:
                return False
            if slow == fast:
                return True
            return twoPoint(slow.next, fast.next.next)
        if not head:
            return False
        return twoPoint(head, head.next)