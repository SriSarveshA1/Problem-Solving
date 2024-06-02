class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)

        i = 0
        j = len_needle-1

        while(j<len_haystack):
            cur_str = haystack[i:j+1]
            if cur_str == needle:
                return i
            
            i+=1
            j+=1
            
        return -1
        