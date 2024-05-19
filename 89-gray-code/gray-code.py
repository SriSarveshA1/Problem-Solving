class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        limit = (1 << n ) -1
        
        i = 0

        result = []

        while(i<=limit):
                
            result.append(i ^ (i>>1))
            i=i+1

        return result    