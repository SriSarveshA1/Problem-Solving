class Solution(object):


    def generate(self,n,res,cur,no_open,no_close):

        if(len(cur)==(n*2)):
            # n = no_of_pairs
            # n*2 is total length of the cur considering all pairs
            string = ""
            for ele in cur:
                string+=ele
            
            res.append(string)
            return
        
        if no_open<n:
            # so there can be open paranthesis upto n, as we want n pairs
            cur.append("(")
            self.generate(n,res,cur,no_open+1,no_close)
            cur.pop()
        
        if no_close<no_open:
            # so there can be close if and only if there are larger no_opening
            # already present and then only if we put close ")" it will be a valid one
            cur.append(")")
            self.generate(n,res,cur,no_open,no_close+1)
            cur.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cur=[]
        res=[]
        self.generate(n,res,cur,0,0)  
        return res