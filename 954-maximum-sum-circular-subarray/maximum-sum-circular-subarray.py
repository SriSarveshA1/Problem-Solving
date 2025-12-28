class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]

        track1 = [0 for i in range(n)]
        track2 = [0 for i in range(n)]

        overall_sum = nums[0]

        # Track from 0 to 1 (including the first element)
        track1[0] = nums[0]
        track2[0] = nums[0]

        max_track1 = nums[0]
        min_track = nums[0]

        for i in range(1,n):
            track1[i] = max(track1[i-1]+nums[i],nums[i])
            max_track1 = max(max_track1,track1[i])

            track2[i] = min(track2[i-1]+nums[i],nums[i])
            min_track = min(min_track,track2[i])

            overall_sum += nums[i]
        
        print("max_track1",max_track1)
        print("overall_sum,", overall_sum)
        print("min_track",min_track)

        # after removing the min_track from overall_sum if the value is 0, then all the elements are 
            # negative and then the max_track1 is the answer
        
        if overall_sum - min_track == 0:
            return max_track1 # what ever kadane found is the possible answer as all are negative

        return max(max_track1, overall_sum - min_track)

        