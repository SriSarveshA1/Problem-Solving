import math

class Solution(object):
    def temp(self,x,N):
        
        if N==1:
            return x
        
        if N==0:
            return 1
        

        ans = self.temp(x, math.floor(N/2))

        if (N%2) == 0:    
            return ans*ans 
        else:
            return ans*ans*x


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 :
            return 1

        if n<1:
            n=-1*n
            return 1/self.temp(x,n)
        
        return self.temp(x,n)
