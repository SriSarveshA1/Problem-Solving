class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        sums = 0
        count = 0
        for ele in nums:
            sums+=ele
            if sums>0:
                count+=1
            else:
                return count
        
        return count



        