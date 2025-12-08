class Solution(object):
    def subarraySum(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        
        prefix_sum = [0 for i in range(n)]
        
        freq_map = dict()
        
        prefix_sum[0] = nums[0]
        freq_map[prefix_sum[0]] = 1
        
        if prefix_sum[0] == target:
            count += 1
        
        # need to find the number of subarrays matching the target 
        
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1]+nums[i]
            
            if prefix_sum[i] == target:
                count+=1
            
            if prefix_sum[i]-target in freq_map:
                count+= freq_map[prefix_sum[i]-target]
                
            
            if prefix_sum[i] in freq_map:
                freq_map[prefix_sum[i]] += 1
            else:
                freq_map[prefix_sum[i]] = 1 
        
        return count
        