class Solution(object):
    def calculate_mid(self,l,r):
        return int(l+((r-l)/2))

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        n = len(nums)

        ans = n

        while l<=r:
            mid = self.calculate_mid(l,r)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid +1
            else:
                ans = mid
                r = mid - 1
        
        return ans
            

        