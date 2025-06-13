class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Find the freq of all chars.
        # Then Try to add all the even chars and if the count is odd just do odd_count-1

        hash_map = dict()

        for char in s:
            if char in hash_map:
                hash_map[char]+=1
            else:
                hash_map[char]=1
        
        length = 0
        for key,value in hash_map.items():
            if value%2 == 0:
                length+=value
            else:
                if length%2 == 0:
                    length+= value
                else:
                    length+= value-1
            
        return length