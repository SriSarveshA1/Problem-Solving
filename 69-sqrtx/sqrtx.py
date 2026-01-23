class Solution:

    def mySqrt(self, x: int) -> int:
        
        l = 1 
        r = x   

        ans = 0

        while(l<=r):
            mid = int((l+r)/2)

            sqr = mid * mid
            if sqr == x:
                return mid
            
            if sqr < x:
                ans = mid
                l = mid+1
            else:
                r = mid-1
            
        return ans

