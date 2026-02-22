class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []

        n = len(nums)

        res = [-1 for i in range(0,n)]


        for i in range((2*n)-1,-1,-1):

            while len(stack) != 0 and stack[len(stack)-1]<= nums[i%n]:
                stack.pop(len(stack)-1) 
            
            if len(stack) == 0:
                res[i%n] = -1
            else:
                res[i%n] = stack[len(stack)-1]   

            stack.append(nums[i%n])


        
        return res
                

