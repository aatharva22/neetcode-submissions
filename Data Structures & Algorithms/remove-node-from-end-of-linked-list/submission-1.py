# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        l = 0
        while curr:
            l = l+1
            curr = curr.next
        if l == 1:

            return None

        curr1 = head.next
        prev = head
        if l - n == 0:
            head = head.next
            return head
        for i in range(1, l-n):
            prev = curr1
            curr1 = curr1.next
        
        #removal
        prev.next = curr1.next
    
        return head