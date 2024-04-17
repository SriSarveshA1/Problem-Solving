class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n

        count = 0

        while(temp>0):
            
            if temp&1 == 1:
                count+=1
            
            temp = temp>>1 
        
        return count


