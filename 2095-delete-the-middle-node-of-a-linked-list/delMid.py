# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None

        if head.next is None:
            return None

        while fast is not None and fast.next is not None:
            prev = slow 
            slow  = slow.next            
            fast = fast.next.next

        prev.next = slow.next
        

        return head

        