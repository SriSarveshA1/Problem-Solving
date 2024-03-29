import math

class Solution(object):
    mod = 1000000007

    def find_factorial(self,n):
        if n==1 or n==0:
            return 1
        
        fact = self.find_factorial(n-1)
        return ( (n%1000000007)*(fact%1000000007) ) % 1000000007

    def find_prime_sieve(self):
        prime_arr = [ True for i in range(101) ]
        prime_arr[0] = False
        prime_arr[1] = False
        
        i = 2
        while(i<=math.sqrt(100)):

            if prime_arr[i] == True:
                j = i*i
                while(j<=100):
                    prime_arr[j] = False
                    j=j+i

            i = i+1
        return prime_arr

    def find_the_no_primes(self,n):
        prime_arr = self.find_prime_sieve()

        no_of_primes = 0

        for i in range(0,n+1):
            if prime_arr[i]:
                no_of_primes +=1
        
        return no_of_primes
        
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=1:
            return 1

        
        no_of_primes = self.find_the_no_primes(n)
        non_primes = n-no_of_primes
        
        prime_combinations = self.find_factorial(no_of_primes)
        non_prime_combinations = self.find_factorial(non_primes)
        return (prime_combinations*non_prime_combinations)%1000000007