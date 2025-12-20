from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    
    def max_sum_sub_tree(self,root,max_v):
        if root == None:
            return 0
        
        sums = root.data + self.max_sum_sub_tree(root.left,max_v)+self.max_sum_sub_tree(root.right,max_v)
        
        max_v[0] = max(max_v[0],sums)
        return sums
        
    
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        
        max_v = [-100000000]
        sums = self.max_sum_sub_tree(root,max_v)
        return max_v[0]
        
        
        
