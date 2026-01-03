'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        
        count = 0
        prev = Node(-1)
        prev.next = head
        cur = head
        
        new_node = Node(x)
        
        while ( count != p+1 and cur != None):
            count += 1
            prev = prev.next
            cur = cur.next
        
        if not cur:
           prev.next = new_node
           new_node.prev = prev
           new_node.next = None
        else:
            prev.next = new_node
            cur.prev = new_node
            new_node.prev = prev
            new_node.next = cur

        
        return head
            
