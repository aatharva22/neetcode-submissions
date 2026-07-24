# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find middle and split the list

        curr = head
        mid = head

        while curr and curr.next:

            mid = mid.next
            curr = curr.next.next
        
        curr = mid.next
        mid.next = None

        #reverse list2
        
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #prev is the start of the reversed list
        list2 = prev
        
        curr = head
        dummy = ListNode(0)
        start = dummy

        while curr and list2:

            temp1 = curr.next
            temp2 = list2.next

            start.next = curr
            start = start.next
            curr = curr.next

            start.next = list2
            start = start.next
            list2 = list2.next

        start.next = curr if curr else list2
        head = dummy.next








        

        

        
