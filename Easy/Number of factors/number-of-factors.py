#User function Template for python3
import math

class Solution:
    def countFactors (self, num):
        # code here
        if num == 1:
            return 1

        count = 0
            
        for i in range(1,int(math.sqrt(num))+1):
            if (num%i == 0):
                if (num/i) == i:
                    count = count + 1
                else:
                    count = count + 2

        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
# } Driver Code Ends