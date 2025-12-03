class Solution(object):

    def generate_subs(self,cur,res,i,k,n):
       
        if i>n:
            if len(cur) == k:
                temp = []
                for v in cur:
                    temp.append(v)
                
                res.append(temp)
            return

        cur.append(i)
        self.generate_subs(cur,res,i+1,k,n)
        cur.pop()

        self.generate_subs(cur,res,i+1,k,n)
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.generate_subs([],res,1,k,n)
        return res
        