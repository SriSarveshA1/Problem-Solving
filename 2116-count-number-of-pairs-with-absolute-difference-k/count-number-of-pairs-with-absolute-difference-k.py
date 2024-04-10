class Solution(object):
    def countKDifference(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        hash_map = dict()
        for num in arr:

            if (num-k) in hash_map:
                count+= hash_map[num-k]
            
            if (num+k) in hash_map:
                count+= hash_map[num+k]
    
            if num in hash_map:
                hash_map[num]= hash_map[num]+1
            else:
                hash_map[num] = 1
        
        return count