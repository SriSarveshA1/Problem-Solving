class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n

        product = 1
        sum_s = 0

        while(n>0):
            rem = n%10
            sum_s+=rem
            product*=rem
            n = n/10
        
        return product - sum_s