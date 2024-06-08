class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0 
        j = n-1

        max_water = -1

        while(i<j):

            water_between_i_and_j = min(height[i],height[j]) * (j-i) 
                                                # (j-i) gives the difference between the two pillers

            max_water = max(water_between_i_and_j,max_water)
            if (height[i]<height[j]):
                i+=1
            else:
                j-=1

        return max_water