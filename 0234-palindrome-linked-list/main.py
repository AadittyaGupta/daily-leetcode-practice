from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        stack = []

        while fast is not None and fast.next is not None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
                slow = slow.next

        while slow is not None:
                top = stack.pop()
                if slow.val != top:
                    return False
                slow = slow.next
        return True