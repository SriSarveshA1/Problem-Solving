class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = dict()
        for num in nums:
            present.update({num:1})
        
        already_visited_nums = dict()

        max_length = 0

        nums = set(nums)

        for num in nums:

            if not ((num+1) in present):

                length = 0
                temp = num
                #already_visited_nums[num] = True
                while temp in present:
                    temp=temp-1
                    length=length+1
                    #already_visited_nums[temp] = True

                max_length = max(max_length,length)
                
        return max_length


