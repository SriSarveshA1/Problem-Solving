class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
        i = 0

        xor = 0
    
        while (n>0):
            cur = start + 2*i
            xor = xor ^ cur

            i = i+1
            n = n-1
        
        return xor