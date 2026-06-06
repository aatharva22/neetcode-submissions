# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle

        fast = head
        slow = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
         # slowis middle

        curr = slow.next 
        slow.next = None
        prev = None

        #reverse 2nd list
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #prev is the start of 2nd half's reversed list

        #merge
        dummy = ListNode(0)
        first = dummy
        curr = head
    
        while prev:
            first.next = curr
            first = first.next
            curr = curr.next

            first.next = prev
            first = first.next
            prev = prev.next
        first.next = curr

            
