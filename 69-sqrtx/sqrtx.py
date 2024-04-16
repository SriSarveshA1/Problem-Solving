class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        

        low = 0
        high = x
        ans = -1
        while(low<=high):
            mid = float(low+(high-low)/2)
            print("low = ",low," mid = ",mid," high = ",high)
            if (mid*mid == x):
                ans = mid
                return int(ans)

            if(mid * mid < x):
                ans = mid
                low = int(mid+1)
            else:
                high = int(mid-1)

        return int(ans)
        