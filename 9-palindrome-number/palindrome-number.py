import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True

        if x<0:
            return False
        
        if x%10 == 0:
            return False

        ori = x
        num = 0
    
        while x>0:
            rem = x % 10
            num = (num*10) +rem
            x = int(x/10)
            
            print("num = ",num)

        
        
        
        if num != ori:
            return False

        return True
            


