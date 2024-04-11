class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        n = len(gain)

        max_sum = 0
        prefix_sum = [0 for i in range(n)]

        prefix_sum[0] = gain[0]
        max_sum = max(max_sum,prefix_sum[0])
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1]+gain[i]
            max_sum = max(max_sum,prefix_sum[i])

        return max_sum





