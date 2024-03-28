class Solution(object):
    def int_to_char(self, n):
        return chr((ord('A')- 1)+n) 
       

    def convertToTitle(self, n):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = ""

        while(n>0):

            rem = n%26
            if rem == 0:
                res += self.int_to_char(26)
            else:
                res += self.int_to_char(rem)

            n = n//26
            if rem == 0:
                n = n-1

        return res[::-1]


        
        