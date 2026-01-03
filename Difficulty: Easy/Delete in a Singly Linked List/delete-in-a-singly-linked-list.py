'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        # edge case
        if x == 1 and head.next == None:
            return None
        
        if x == 1:
            head = head.next
            return head
        
        
        prev = Node(-1)
        prev.next = head
        cur = head
        count = 1
        
        while count!=x and cur.next != None:
            
            prev = prev.next
            cur = cur.next
            count+=1
        
        prev.next = cur.next
        return head
        
        
