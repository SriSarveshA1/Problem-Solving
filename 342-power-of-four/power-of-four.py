class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n==1):
            return True
        if (n<4):
            return False
        
        no_of_bits_that_make_up = int(math.log2(n)) + 1 
        print("no_of_bits_that_make_up = ",no_of_bits_that_make_up)

        if (n&(n-1)) == 0 and (no_of_bits_that_make_up%2 != 0):
            return True
        else:
            return False