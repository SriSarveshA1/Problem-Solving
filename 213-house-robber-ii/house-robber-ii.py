class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]

        if n==1:
            return nums[0]
        
        if n==2:
            return max(nums[0],nums[1])
        
        dp1[0] = nums[0] # picking the 0th
        dp1[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            dp1[i] = max(dp1[i-1],nums[i]+dp1[i-2])
        
        dp1[n-1] = dp1[n-2] 

        reversed_list = nums[::-1]

        dp2[0] = reversed_list[0] #picking the last element
        dp2[1] = max(reversed_list[1],reversed_list[0])

        for i in range(2,n-1):
            dp2[i] = max(dp2[i-1],reversed_list[i]+dp2[i-2])
        
        dp2[n-1] = dp2[n-2]

        return max(dp1[n-1],dp2[n-1])
