import math
class Solution:

    def find_first_occurance(self,nums,target):
        index = -1

        low = 0
        high = len(nums)-1

        while(low<=high):
            mid = math.floor((low+high)/2)
            
            if(nums[mid]==target):
                index = mid

            if (nums[mid]>=target):
                high = mid-1
            else:
                low = mid+1

        return index
    
    def find_last_occurance(self,nums,target):
        index = -1

        low = 0
        high = len(nums)-1

        while(low<=high):
            mid = math.floor((low+high)/2)

            if(nums[mid]==target):
                index = mid

            if(nums[mid]<=target):
                low = mid+1
            else:
                high = mid-1
        
        return index




    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        first = self.find_first_occurance(nums,target)
        secound = self.find_last_occurance(nums,target)

        return [first,secound]