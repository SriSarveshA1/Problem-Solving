class Pair:
    def __init__(self,*,index,value):
        self.index = index
        self.value = value

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_list = []
        min_list = []
        l = 0
        r = 0 

        res = -1

        n = len(nums)

        while(r<n):

            while( max_list and max_list[len(max_list)-1].value < nums[r]):
                last_index = len(max_list)
                max_list.pop(last_index-1)
            
            max_list.append(Pair(index=r,value=nums[r])) 

            while( min_list and min_list[len(min_list)-1].value > nums[r]):
                last_index = len(min_list)
                min_list.pop(last_index-1)

            min_list.append(Pair(index=r,value=nums[r]))

            while abs(max_list[0].value - min_list[0].value) > limit:

                if max_list[0].index == l:
                    print(True) if max_list[0].index < l else ""

                    max_list.pop(0)
                
                if min_list[0].index == l:
                    print(True) if min_list[0].index < l else ""
                    min_list.pop(0)

                l+=1
            
            
            res = max(res,(r-l)+1)
            r+=1

        return res

            

