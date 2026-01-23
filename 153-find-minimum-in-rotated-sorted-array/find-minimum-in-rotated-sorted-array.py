import math

class Solution:

    def calculate_mid(self,l,r):
        mid = math.floor(l + ((r-l)/2))
        return mid

    
    def is_min(self,nums,n,mid):
        if (mid-1 < 0) and (mid+1 > n-1):
            return True
        
        if (mid-1<0) and (mid+1 <=n-1) and (nums[mid]<nums[mid+1]):
            return True
        
        if (mid-1>=0) and (mid+1 > n-1) and (nums[mid-1] > nums[mid]):
            return True
        
        if (mid-1>=0 and mid+1<=n-1 and nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]):
            return True
        


    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while(l<=r):
            mid = self.calculate_mid(l,r)

            if self.is_min(nums,n,mid):
                return nums[mid]
            
            if nums[l] <= nums[mid]:
                if nums[l]>nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                r = mid-1

        return -1 



        