# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        n = head

        while n.next:
            res.append(n)           
            n = n.next
        res.append(n) #[1,2,3,4,5]

        return res[(len(res)//2)]