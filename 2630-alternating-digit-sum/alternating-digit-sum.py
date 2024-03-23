import math

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        no_d = int(math.log10(n))+1

        
        if (no_d%2)!=0:
            start_sign = -1
        else:
            start_sign = 1

        sum_s = 0
        num = n
        while(n>0):
            rem = n%10
            start_sign*=-1
            sum_s +=start_sign* rem
            n = n/10
        
        return sum_s

        