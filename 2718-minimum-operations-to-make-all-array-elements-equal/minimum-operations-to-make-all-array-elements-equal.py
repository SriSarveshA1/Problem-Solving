class Solution:
    def calculate_mid(self,l,r):
        size = (r-l)+1
        if (size%2) == 0:
            return math.floor(l+((r-l)/2))

        return math.floor(l+((r-l+1)/2))

    def left_bigger_index(self,arr: [int], x: int, n: int) -> int:
        # Write your code here.
        l = 0
        r = len(arr)-1

        ans = -1

        while(l<=r):
            mid = self.calculate_mid(l,r)

            if(arr[mid]>=x):
                r = mid-1
            else:
                ans = mid
                l = mid+1

        if r<0:
            return -1

        if l>=n:
            return -1

        return ans

    def right_smaller_index(self,arr,x,n):
        l = 0
        r = len(arr)-1

        ans = -1

        while(l<=r):
            mid = self.calculate_mid(l,r)

            if(arr[mid]<=x): 
                l = mid+1 
            else:
                ans = mid # Possible answer 
                r = mid - 1

            # if(arr[mid]>=)

        if r<0:
            return -1

        if l>=n:
            return -1

        return ans

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # left biggest index of nums[i]
        # right smaller index of nums[i]

        n = len(nums)
        nums = sorted(nums)
        overall_sum = 0

        prefix_sum = [0 for i in nums]
        prefix_sum[0] = nums[0]
        overall_sum = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
            overall_sum += nums[i]

        
        result = []
        
        for target in queries:
            
            if target<nums[0] or target>nums[n-1]:
                ans = abs( target*n - overall_sum)
                result.append(ans)
                continue
            
            left_bigger_index = self.left_bigger_index(nums, target, n)
            right_smaller_index = self.right_smaller_index(nums, target, n)
           # print("left_bigger_index= ",left_bigger_index)
           # print("right_smaller_index= ",right_smaller_index)

            cur_ans = 0

            if left_bigger_index != -1 and left_bigger_index<=n-1:
                no_till_left_big_idx = left_bigger_index+1

               # print(" prefix_sum[left_bigger_index] = ", prefix_sum[left_bigger_index])

                cur_ans += abs(no_till_left_big_idx*target - prefix_sum[left_bigger_index])
            
            if right_smaller_index != -1 and right_smaller_index>=0:
                ref_idx = right_smaller_index-1 # index just before the right_smaller_index
                print("prefix_sum[n-1]-prefix_sum[ref_idx] = ",prefix_sum[n-1]-prefix_sum[ref_idx])
                sum_from_the_right_smaller_index_to_end = prefix_sum[n-1]-prefix_sum[ref_idx]

                numbers_from_right_smaller_index_to_end = n-right_smaller_index

                cur_ans += abs(numbers_from_right_smaller_index_to_end*target - sum_from_the_right_smaller_index_to_end )

            result.append(cur_ans)
        
        return result











