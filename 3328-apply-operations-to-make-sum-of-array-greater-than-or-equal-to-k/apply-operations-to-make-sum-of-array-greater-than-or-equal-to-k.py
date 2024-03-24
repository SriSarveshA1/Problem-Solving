import math

class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        cur_v = 1
        
        no_ops = 0
        
        result = 100000007
        
        i = 1
        
        
        while(i<=k):
            
          
            
            cur_ops1 = no_ops + (k-cur_v)
            
            if(k%cur_v) == 0:
                cur_ops2 = no_ops + (k/cur_v)-1
            else:
                cur_ops2 = no_ops + ((k/cur_v)) 
            
            total_ops = min(cur_ops1,cur_ops2)
            
            print("cur_v = ",cur_v ," total_ops = ",total_ops)
            
            if(total_ops>result):
                break

            result = min(result,total_ops)
            
        
            i=i+1
            cur_v+=1
            no_ops+=1
            
            
            
        
        return result