class Solution(object):
    def is_digit(self,ch):
        if ord(ch) >=48 and ord(ch)<=57:
            return True
        
        return False
    
    def is_white_space(self,ch):
        if ch == '' or ch == " ":
            return True
        
        return False

    def atoi_func(self,n,s,cur,i):

        if i>=n:
            return
        
        ch = s[i]
        
        if len(cur)==0 and (self.is_white_space(ch)):
            # Skipping leading white space or 0's
            print("skipping white space",i)
            self.atoi_func(n,s,cur,i+1)

        elif ((ch == '-' or ch == '+') and len(cur)==0) or self.is_digit(ch):
            # 1. Sign is added only if the length of cur is 0
            # 2. Or just add the digit character ,if there is alreayd ele in cur

            cur.append(ch)
            self.atoi_func(n,s,cur,i+1)

        elif (not self.is_digit(ch) and len(cur)>0):
            # we stop if we find any non-digit character inbetween
            print("found non-digit char ",i)
            return
        
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Iterate the characters in 's' if there are '' whitespace ignore it
        # And basically try to find first index which has a digit character.

        cur = []

        self.atoi_func(len(s),s,cur,0)
        print("cur = ",cur)
        if len(cur) == 0:
            return 0
        
        string = ""
        count_of_digits = 0
        for ele in cur:
            string+=ele
            if self.is_digit(ele):
                count_of_digits+=1

        if count_of_digits==0:
            return 0

        result = int(string)

        if result< pow(-2,31):
            result = pow(-2,31)
        elif result > (pow(2,31)-1):
            result = (pow(2,31)-1)
        
        return result
        