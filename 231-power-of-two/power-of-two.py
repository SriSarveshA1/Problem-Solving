class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            # for negative numbers 
            # and zero we can't represent that in power of 2
            return False
        
        if (n&(n-1)) == 0:
            return True
        
        return False