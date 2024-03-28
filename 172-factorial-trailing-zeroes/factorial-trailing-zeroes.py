import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        i = 5
        while True:
            division = int(math.floor(n//i))
            res += division
            i = i*5
            if division == 0 :
                return res
        
        return res
        
        return res

        
