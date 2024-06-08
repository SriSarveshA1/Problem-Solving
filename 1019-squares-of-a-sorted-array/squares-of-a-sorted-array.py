class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        j = n-1

        res=[0 for o in range(0,n)]
        
        k = n-1

        while(i<=j):

            left = nums[i]*nums[i]
            right = nums[j]*nums[j]

            if(left<=right):
                res[k]=right
                j-=1
            else:
                res[k]=left
                i+=1
            
            k-=1
        
        return res