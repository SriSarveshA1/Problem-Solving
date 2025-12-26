class Solution:

    def check_if_partition_is_palindrome(self,string):
        n = len(string)
        l = 0
        r = n-1

        while l<=r:
            if string[l] == string[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True

    def generate_partitions(self,s,start,cur,res,n):
        if start>=n:
            # we are in terminal state 
            if len(cur)>=1:
                res.append(cur.copy())
            
            return 
        
        for i in range(start,n):

            if self.check_if_partition_is_palindrome(s[start:i+1]):
                # all the partitions that we make in a path should be palindrome for sure
                cur.append(s[start:i+1])
                self.generate_partitions(s,i+1,cur,res,n)
                cur.pop()
            else:
                # For the index [start to i] if its not palindrome then the recursions that could happen in that
                # path we no need to calculate
                continue
            


    def partition(self, s: str) -> List[List[str]]:
        cur = []
        res = []
        n = len(s)
        self.generate_partitions(s,0,cur,res,n)
        return res
        