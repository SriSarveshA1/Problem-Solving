class Solution:

    def find_0(self,index,nums):
        n = len(nums)

        for i in range(index,n):
            if nums[i] == 0:
                return i
        
        return -1
    
    def find_1(self,index,nums):
        n = len(nums)

        for i in range(index,n):
            if nums[i] == 1:
                return i
        
        return -1



    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        find_0 = True
        index = 0
        
        while index!=-1:
            
            if find_0:
                ans = self.find_0(index,nums)
                
                find_0 = False
                index = ans
            else:
                ans = self.find_1(index,nums)
                find_0 = True
                index = ans

            if index!=-1:
                operations+=1

        
    
        return operations