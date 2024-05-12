class Solution(object):
    def subarraySum(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = dict()
        
        prefix_sum = arr[0]
        

        count = 0

        hash_map[prefix_sum] = 1
        
        if prefix_sum == k:
            count+=1
        
        for i in range(1,len(arr)):
            
            prefix_sum += arr[i]
            if prefix_sum == k:
                count+=1
            
            if(prefix_sum-k) in hash_map:
                count+=hash_map[prefix_sum-k]


            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = 1
            else:
                hash_map[prefix_sum]=hash_map[prefix_sum]+1
        
        return count