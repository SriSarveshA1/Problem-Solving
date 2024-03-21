# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.next == None:
            return head    

    
        temp = None
        p1 = head
        p2 = head.next

        while(p1!=None):
            p1.next = temp
            temp = p1
            p1 = p2

            if p2 != None:
                p2 = p2.next

        return temp