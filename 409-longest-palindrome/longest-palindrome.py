class Solution(object):
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: int
        """
        hash_map = dict()
        pair_count = 0
        for char in string:
            # basically we are finding how many pairs for each character that is appearing

            if char in hash_map:
                # if a particular char appears again then its part of the pair
                
                pair_count+=1 #so we increase the total pairs count
                del hash_map[char]
            else:
                hash_map[char]=1
        
        if len(hash_map)!=0:
            return (pair_count*2)+1
        
        return (pair_count*2)