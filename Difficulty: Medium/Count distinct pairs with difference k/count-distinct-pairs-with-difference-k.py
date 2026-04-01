#User function Template for python3
from collections import defaultdict

class Solution:
    
    def return_formed_tuple(self,ele1,ele2):
        first = max(ele1,ele2)
        sec = min(ele1,ele2)
        return (first,sec)
    
	def TotalPairs(self, nums, k):
		# Code here
		
		hash_map = defaultdict(int)
		
		for ele in nums:
		    hash_map[ele]+=1
		   
		tuple_set = set()
		
		nums.sort()
		
		n = len(nums)
		
		count = 0 
		
		# a - b = k, we will construct k +b and find a is there in hash_map
		
		for ele in nums:
		    
		    formed_tuple = self.return_formed_tuple(ele,k+ele)
		    
		    if k+ele in hash_map and formed_tuple not in tuple_set:
		        if k+ele == ele and k == 0 and hash_map.get(ele) < 2:
		            continue # its not a pair
		        
		        tuple_set.add(formed_tuple)
		        count+=1
		
		return count
		      
		        
		        
		        
		        
		    

		