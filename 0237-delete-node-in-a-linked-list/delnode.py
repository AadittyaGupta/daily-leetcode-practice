# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # temp = node
        # prev = node

        # temp = temp.next

        # prev.val = temp.val

        # prev.next = prev.next.next
        

        node.val = node.next.val
        node.next = node.next.next