class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []

        res = []

        hash_map = dict()

        n = len(nums)

        for i in range((2*n)-1,-1,-1):

            while len(stack) != 0 and stack[len(stack)-1]<= nums[i%n]:
                stack.pop(len(stack)-1) 
            
            #if i%n not in hash_map or hash_map[i%n] == -1 :
            if len(stack) == 0:
                    hash_map[i%n] = -1
            else:
                    hash_map[i%n] = stack[len(stack)-1]   

            stack.append(nums[i%n])

        for i in range(0,len(nums)):
            res.append(hash_map[i])
        
        return res
                

