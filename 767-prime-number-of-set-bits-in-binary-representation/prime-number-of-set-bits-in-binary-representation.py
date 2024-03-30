import math

class Solution(object):

    def countFactors(self, num):
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

    def checkIfPrime(self,num):

        counter = self.countFactors(num)
        if counter==2:
            return True
        
        return False


    def count_set_bits(self,num):

        temp = num

        count = 0

        while(temp>0):
            
            if temp&1 == 1:
                count+=1
            
            temp = temp>>1

        return count

    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        for num in range(left,right+1):
            no_set_bits = self.count_set_bits(num)
            if self.checkIfPrime(no_set_bits):
                res = res+1
        
        return res