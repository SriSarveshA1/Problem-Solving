# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = []

        queue.append(root)

        root.level = 1



        level_sum = dict()


        while(len(queue) != 0):

            node = queue.pop(0)
            
            current_level = node.level

            if not current_level in level_sum:
                level_sum[current_level] = node.val
            else:
                level_sum[current_level] += node.val

            if node.left:
                node.left.level = current_level+1
                queue.append(node.left)
            
            if node.right:
                node.right.level = current_level+1
                queue.append(node.right)
            

        max_sum = -100000000
        min_level = 1
        for level,sum_value in level_sum.items():
            if sum_value>max_sum:
                max_sum = sum_value
                min_level = level

        return min_level


            

