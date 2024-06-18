class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_array = [0 for i in range(len(nums))]
        prefix_array[0]=nums[0]
        
        for i in range(1,len(nums)):
            prefix_array[i] = prefix_array[i-1] + nums[i]
        print(prefix_array)
        for i in range(0,len(nums)):
            prefix_array[i] = prefix_array[i] % k
       
        hash_map = dict()
        count = 0
        
        for i in range(0,len(nums)):
            num_mod_k = prefix_array[i] % k
            
            if num_mod_k == 0: # corner case
                count+=1 # To find the subarray from [0,i]
                        # The subarray from ([0,i] % k) ==0
                        # We are counting this seperately

            if num_mod_k in hash_map:
                # finding whether subarray[i] that exists or not
                count+= hash_map[num_mod_k]
                hash_map[num_mod_k] = hash_map[num_mod_k] + 1
            else:
                hash_map[num_mod_k] = 1

        return count
        
        
