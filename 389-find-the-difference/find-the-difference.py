class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_map = dict()
        for char in s:
            if char in hash_map:
                hash_map[char] = hash_map[char] + 1
            else:
                hash_map[char] = 1
            
        
        for char in t:
            if char not in hash_map:
                return char 
            
            if char in hash_map:
                hash_map[char] = hash_map[char] - 1
                if hash_map[char] == 0:
                    del hash_map[char] 

        print(hash_map)