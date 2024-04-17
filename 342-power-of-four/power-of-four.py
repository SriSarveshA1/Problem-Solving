class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n==1):
            return True
        if (n<4):
            return False
       
        if (n&(n-1)) == 0 and (n%3 == 1):
            return True
        else:
            return False