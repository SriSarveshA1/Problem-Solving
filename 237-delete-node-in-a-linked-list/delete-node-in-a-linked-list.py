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
        
        prev = ListNode(-100000)
        prev.next = node
        cur = node

        while cur.next != None:
            cur.val = cur.next.val
            prev = prev.next
            cur = cur.next
        
        prev.next = None
        
        
