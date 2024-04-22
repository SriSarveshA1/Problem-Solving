class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        count = 0

        count_of_set_bits = [0 for i in range(0,32)] # count of set bits at each bit
        count_of_unset_bits = [0 for i in range(0,32)] # n-count_of_set_bits[i] will be the count of unset bits in
                                    # the provided list of numbers
        for i in range(0,31):
            count_of_set_bits[i] = 0
            for num in nums:
                # there are total 32 bits.
                # if we right shigt n>>i will give value of the ith bit
                count_of_set_bits[i] += 1 if ((num&(1<<i)))>0 else 0 # initially we will only count the no of set bits
                # later we calculate the unset bits from the count_of_set_bits

        

        res = 0 # we can also calculate the overall answer 
        for i in range(0,31):
            count_of_unset_bits[i] = abs(n - count_of_set_bits[i])
            res += count_of_set_bits[i] * count_of_unset_bits[i]

        print(count_of_set_bits)
        print(count_of_unset_bits)
           
        return res