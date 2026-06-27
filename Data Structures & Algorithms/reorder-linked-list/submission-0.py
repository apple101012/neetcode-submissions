# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        prev = None
        # reverse second
        while second: 
            next_ = second.next
            second.next = prev
            prev = second
            second = next_
        
        first = head
        second = prev
        while second:
            n1 = first.next
            n2 = second.next
            first.next = second
            second.next = n1
            first = n1
            second = n2
        



                