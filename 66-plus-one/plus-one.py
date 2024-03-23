class Solution(object):
    def plusOne(self, arr):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        i = n-1

       
        while(i>=0):
            if(arr[i]!=9):
                arr[i]=1+arr[i]
                return arr
            else:
                if(arr[i]==9):
                    arr[i]=0
                    rem = 1
            i=i-1
        
        if rem==1:
            return [1]+arr
        
        return arr