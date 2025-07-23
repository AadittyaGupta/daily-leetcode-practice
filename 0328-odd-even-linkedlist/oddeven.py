from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None:     #edge case
        #     return head

        # temp = head
        # my_list = []

        # while temp and temp.next :       # for odd value
        #     my_list.append(temp.val)
        #     temp = temp.next.next
        # if temp != None:
        #     my_list.append(temp.val)

        # temp = head.next
        # while temp and temp.next :        # for even value
        #     my_list.append(temp.val)
        #     temp = temp.next.next
        # if temp != None:
        #     my_list.append(temp.val)


        # temp = head
        # index = 0
        # while temp is not None:
        #     temp.val = my_list[index]
        #     index += 1
        #     temp = temp.next

        # return head
        
        if head is None or head.next is None:
            return head
        # even_head = head.next
        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head
