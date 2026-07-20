# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
            if not node1:
                return node2
            elif not node2:
                return node1
            val1, val2 = node1.val, node2.val
            if val1 < val2:
                node1.next = merge(node1.next, node2)
                return node1 
            node2.next = merge(node1, node2.next)
            return node2
        return merge(list1, list2)