class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0 
        j = n-1

        max_water = -1

        while(i<j):

            water_between_i_and_j = min(nums[i],nums[j]) * (j-i)

            max_water = max(water_between_i_and_j,max_water)
            if (nums[i]<nums[j]):
                i+=1
            else:
                j-=1

        return max_water