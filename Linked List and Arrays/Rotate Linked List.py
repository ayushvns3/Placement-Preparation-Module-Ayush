# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head:
            return head
        n=head
        count = 1
        while n.next:
            n=n.next
            count += 1
        #print(count)
        n.next=head
        n=head
        rem = k%count
        for _ in range(count-rem-1):
            n = n.next
        temp = n.next
        n.next = None
        return temp
        