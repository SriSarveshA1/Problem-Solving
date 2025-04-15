class Solution:

    def helper(self,*,first_len,second_len,nums) -> int:
        n = len(nums)

        p_left = [-1 for i in nums]

        p_left[first_len-1] = 0
        for i in range(0, first_len):
            p_left[first_len-1] += nums[i]

        # p_left[i] gives what is the maximum sum subarray ending at that index i of length firstLen
        for i in range(first_len, n):
            p_left[i] = ( nums[i] + p_left[i-1] ) - nums[i-first_len]
        
        print("p_left = ",p_left)

        max_left = [-1 for i in nums]

        max_left[first_len-1] = p_left[first_len-1]

        for i in range(first_len, n):
            max_left[i] = max(max_left[i-1],p_left[i])
        
        print("max_left = ",max_left)
        # ----

        p_right = [-1 for i in nums]

        p_right[n-second_len] = 0
        for i in range(n-second_len,n,1):
            p_right[n-second_len] += nums[i]
        
        # p_right[i] gives what is the maximum sum subarray starting at index i of length secondLen
        for i in range(n-second_len-1,-1,-1):
            p_right[i] = (nums[i] + p_right[i+1]) - nums[i+second_len]

        print("p_right = ",p_right)

        max_right = [-1 for i in nums]

        max_right[n-second_len] = p_right[n-second_len]

        for i in range(n-second_len-1,-1,-1):
            max_right[i] = max(max_right[i+1],p_right[i])

        print("max_right = ",max_right)

        final_ans = -1
        for i in range(0,n):
            if i == n-1:
                cur_sum = max_left[i]
            else:
                cur_sum = max_left[i] + max_right[i+1]
            final_ans = max(cur_sum,final_ans)

        return final_ans

    def maxSumTwoNoOverlap(self, nums: List[int], first_len: int, second_len: int) -> int:
        ans1 = self.helper(first_len=first_len,second_len=second_len,nums=nums)
        ans2 = self.helper(first_len=second_len,second_len=first_len,nums=nums)    
        print

        return max(ans1,ans2)
