class Solution(object):

    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = dict()

        n = len(s)

        idx = 0 # we have an assumption that idx index character is holding the answer
                # and initially we have the idx as 0

        for i in range(0,n):

            # when ever we see a character we try to increase its frequency
            if s[i] in freq:
                freq[s[i]] = freq[s[i]] + 1
            else:
                freq[s[i]] = 1
            
            if (s[idx] in freq) and freq[s[idx]] > 1: # and if our current character(assumptioned index character ) freq > 1
                # which means we need to find the next correct value for idx whose occurence is freq==1
                idx=idx+1
                while(idx<n):
                    # we stop this loop as soon as freq[idx]<=1
                    if (s[idx] not in freq) or (freq[s[idx]] == 1):
                        # so we are increaing the freq of idx character
                        break

                    idx = idx+1
                
                if idx == n:
                    return -1 # which means we reach the end and didn't find any char with freq==1
            
            

        return idx

      
            
