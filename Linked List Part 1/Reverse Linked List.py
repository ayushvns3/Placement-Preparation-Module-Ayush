# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        n = head
        while n:
            lost_pointer = n.next
            n.next = prev
            prev = n
            n = lost_pointer
        return prev