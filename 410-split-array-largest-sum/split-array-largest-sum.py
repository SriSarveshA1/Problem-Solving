import math

class Solution:
    def find_partitions(self,mid,nums):
        partitions = 1
        sum_of_array = 0
        for i in range(0,len(nums)):
            if(sum_of_array+nums[i]<=mid):
                sum_of_array = sum_of_array+nums[i]
            else:
                partitions+=1
                sum_of_array = nums[i]
            
                
        
        return partitions

    
    def splitArray(self, nums: List[int], k: int) -> int:
        
        min_value = -1
        sum_of_elements = 0
        for num in nums:
            min_value = max(min_value,num)
            sum_of_elements += num 
        
        low = min_value
        high = sum_of_elements 
        
        ans = -1

        while(low<=high):
            mid = int((low+high)/2)
            partitions = self.find_partitions(mid,nums)
            print("mid = ",mid)
            print("partitions = ",partitions)
            if partitions <=k:
                ans = mid
                high = mid-1
            elif partitions > k:
                low = mid+1 
           
                

        
        return ans

