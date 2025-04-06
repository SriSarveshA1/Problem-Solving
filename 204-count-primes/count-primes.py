import math

class Solution:
    
    def create_empty_seive_array(self,n:int)-> list[bool]:
        prime_array = []
        for i in range(0,n+1):
            prime_array.append(True)
        
        prime_array[0] = False
        prime_array[1] = False

        return prime_array

    
    def fill_sieve_array(self,n,prime_array:list[bool])-> None:
        
        for i in range(2,int(math.sqrt(n))+1):

            if i !=2 and i%2 == 0:
                continue
    
            if not prime_array[i]:
                continue

            for j in range(i*i, n+1, i):
                prime_array[j] = False



    def countPrimes(self, n: int) -> int:
        if n == 0 or n==1:
            return 0

        prime_array = self.create_empty_seive_array(n)
        self.fill_sieve_array(n,prime_array)

        count = 0

        for i in range(len(prime_array)):
            if prime_array[i] and i<n:
                count+=1
        
        return count


