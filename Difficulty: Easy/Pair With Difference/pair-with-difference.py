
from typing import List
import math


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        
        i = 0 
        j = 1 
        
        arr.sort()
        
        n =len(arr)
        
        res = False
        
        while i<j and j<n:
            
            diff = abs(arr[i] - arr[j])
            if diff == x:
                return True
            
            if diff < x:
                j+=1
            else:
                i+=1
            
            if i==j:
                j+=1
            
        
        return res
        
