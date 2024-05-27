class Solution(object):

    def find_no_occ(self,nums,compare_key):
        count = 0

        for ele in nums:
            if ele>=compare_key:
                count+=1
        
        return count


    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        
        for i in range(1,max_num+1):
            num = i
            if self.find_no_occ(nums,num) == num:
                    return num

        return -1