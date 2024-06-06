import math

class Solution(object):

    def gcd(self, a, b):
        divisor = min(a,b)
        divident = max(a,b)
        while(True):
            if ( (divident % divisor) == 0 ):
                return divisor
            if ( (divident % divisor) == 1 ):
                return 1
            
            reminder = divident % divisor
            divident = divisor
            divisor = reminder

    def lcm(self, a, b):
        return (a*b)/self.gcd(a,b)
                
    def calculate_number_of_multiples(self,N,a,b):
        return math.floor(N/a) + math.floor(N/b) - math.floor(N/(self.lcm(a,b)))
 
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        low = min(a,b)
        high = min(a,b)*n
        ans = -1
        while(low<=high):
            mid = (low+((high-low)/2))

            count_multiples_a_b = self.calculate_number_of_multiples(mid,a,b)

            if(count_multiples_a_b >= n):
                ans = mid # trying to find the first appearing maginal number
                          # that have 'n' multiples from [1,mid] range
                high = mid - 1
            else:
                if count_multiples_a_b < n:
                    low = mid + 1
                
            
        return ans % 1000000007



        