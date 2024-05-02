class Solution:

    def get_mid(self, low, high):
        length_search_space = (low+high)+1
        if (length_search_space%2)==0:
            #even
            mid = int(low+(high-low)/2)
        else:
            mid = int(low+(high-low+1)/2) 
        
        return mid

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n-1

        while(low<=high):
            mid = self.get_mid(low,high)
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
        
        return low