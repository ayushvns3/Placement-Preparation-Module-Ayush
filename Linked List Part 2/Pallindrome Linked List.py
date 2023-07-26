# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = head
        res = []
        while n.next:
            res.append(n.val)
            n = n.next
        if n.next == None:
            res.append(n.val)
        rev = res[::-1]
        if rev == res:
            return True
        else:
            return False

