class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        minimum_freq = dict()
        for char in range(97,123):
            # we can store the frequence of each char as 1000
            # So that at each word the length of each char at max can be 100
            # so storing it as 1000 can be used for calculation
            minimum_freq[chr(char)] = 1000 
        

        for word in words:
            freq = dict()
            for char in word:
                if char in freq:
                    freq[char] = freq[char] + 1
                else:
                    freq[char] = 1
            
            # Then we need to iterate from 'a' to 'z' and see the minimum freq of 
            # chars appearing in each and every word
            for char in range(97,123):
                if chr(char) in freq:
                    minimum_freq[chr(char)] = min(freq[chr(char)],minimum_freq[chr(char)])
                else:
                    # which means this particular is not appearing in that word
                    # which means it can't be common accross all the words
                    minimum_freq[chr(char)] = 0

        # atlast the minimum_freq will be storing common char in every word and its minimum 
            # freq across all the words
        
        res = []
        for char in range(97,123):
            # we iterate every character 
            # and find the char whose freq > 0
            if minimum_freq[chr(char)]>0:
                frequency = minimum_freq[chr(char)]
                while(frequency>0):
                    res.append(chr(char))
                    frequency-=1

        return res
            