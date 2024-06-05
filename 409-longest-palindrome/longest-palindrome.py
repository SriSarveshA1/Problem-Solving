class Solution(object):
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: int
        """
        hash_map = dict()
        pair_count = 0
        for char in string:
            if char in hash_map:
                del hash_map[char]
                pair_count+=1
            else:
                hash_map[char]=1
        
        if len(hash_map)!=0:
            return (pair_count*2)+1
        
        return (pair_count*2)