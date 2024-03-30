class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        present = dict() # This holds whether a number is present in the array

        checked_for_sequence = dict() # this holds whether a number is checked whether
                                    # it is a part of a ongoing consecutive sequence
                                    # so if we come across this element while iterating 
                                    # we skip it.
        for num in nums:
            if num not in present:
                present[num] = True
        
        max_length = 0

        # So now the idea is basically we need to iterate the array and check whether
        # there could be a potential consecutive sequence that could start from that number

        # To check that if present[num-1] == false which means the previous element of that
        # num is not present in the array so we can check whether this num is the start of sequence

        # and if present[num-1] == true if the previous element of num is present then means
        # the num is already a part of sequence so we skip the sequence check of this num

        for num in nums:

            if (num not in checked_for_sequence) and ((num-1) not in present):
                # which means the num is not part of an consecutive sequence
                # and the (num-1) is not even exists so the "num" could be the potential
                # start of a sequence
                
                temp = num
                length = 0
                while((temp in present)):
                    # so while the consequtive elements are present we run this loop 
                    # and mark the consequtive sequence and also track the length of the 
                    # sequence
                    checked_for_sequence[temp] = True
                    temp = temp+1
                    length = length+1

                max_length = max(max_length,length)

        return  max_length