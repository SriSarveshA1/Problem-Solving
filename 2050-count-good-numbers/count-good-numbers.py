class Solution(object):

    def calculate_powers(self,x,n):
        mod = 1000000007

        if n == 0:
            return 1

        if n == 1:
            return x
        
        ans = self.calculate_powers(x,n//2)

        if n%2 == 0:
            return ((ans%mod) * (ans%mod)) % mod
        
        return ((ans%mod)*(ans%mod)*(x%mod)) % mod

    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 1000000007

        if n == 1:
            return 5

        no_of_even = None
        no_of_odd = None
        
        if n%2 != 0:
            no_of_even = math.floor(((n-1)/2)+1)
            no_of_odd = n - no_of_even
        else:
            no_of_even = n/2
            no_of_odd = no_of_even
        
        print("no_of_even = ",no_of_even)
        print("no_of_odd = ",no_of_odd)

        pow_5 = self.calculate_powers(5,no_of_even) 
        pow_4 = self.calculate_powers(4,no_of_odd)

        print("pow_5 = ",pow_5)
        print("pow_4 = ",pow_4)

        return (pow_4  * pow_5 ) % mod

        
        

        