"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here 
        
        if head.next == None:
            return head
            
        
        cur = head
        while(cur.next != None):
            cur = cur.next
        
        tail = cur
        
        prev = Node(-1)
        
        rev_cur = tail
        prev.next = rev_cur
        
        while(rev_cur != None):
            temp = rev_cur.next
            rev_cur.next = rev_cur.prev
            rev_cur.prev = temp
            
            rev_cur = rev_cur.next
            prev = prev.next
            
            
        return tail
        
            
        
        
        
        