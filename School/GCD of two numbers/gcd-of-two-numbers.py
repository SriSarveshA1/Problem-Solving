
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if a==0:
            return b
            
        if b==0:
            return a
            
        divisor = min(a,b)
        divident = max(a,b)
        

        
        while True:
            
            if divident % divisor == 0:
                return divisor
            
            if divident % divisor == 1:
                return 1
            
            
            reminder = divident % divisor
            divident = divisor
            divisor = reminder
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends