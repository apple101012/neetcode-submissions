# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = head.next
        prev = None
        curr = head
        while(curr.next != None):
            n = curr.next
            curr_ = curr
            curr.next = prev
            prev = curr_
            curr = n
        curr.next = prev
        return curr