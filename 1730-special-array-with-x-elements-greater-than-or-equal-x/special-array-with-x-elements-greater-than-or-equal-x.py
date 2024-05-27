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
        hash_map = dict()
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        for key in hash_map:
            num = key
            count = hash_map[num]

            if count == 1:
                if self.find_no_occ(nums,num) == num:
                    return num
        
        for i in range(1,1001):
            num = i
            if self.find_no_occ(nums,num) == num:
                    return num

        return -1