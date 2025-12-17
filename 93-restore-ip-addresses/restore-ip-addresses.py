import math

class Solution(object):

    def no_digits(self,cur):
        if len(cur)>0:
            cur = int(cur)
            if cur == 0:
                return 1
            return int(math.log10(cur))+1
        return 0



    def is_valid_ip(self,string):
        
        splits = []
        cur = ""
        
        for ch in string:
            if ch == '.':
                if len(cur) > 3:
                    return False
                
                if len(cur)>0 and int(cur)>255:
                    return False
                
                if len(cur) != self.no_digits(cur):
                    return False
                
                splits.append(cur)
                cur = ""
                continue
            
            cur= cur +""+ ch 
        
        if cur!="":
            if len(cur) > 3:
                return False
                
            if len(cur)>0 and int(cur)>255:
                return False
                
            if len(cur) != self.no_digits(cur):
                return False
                
            splits.append(cur)
            
        # print("splits = ",splits)

        if len(splits)!= 4:
            return False
        
        return True
    
    
    def generate_all_ips_by_validating(self,string,res,cur):
        #print("string = ",string)

        n = len(string)
        
        if n<=0:
            if self.is_valid_ip(cur):
                print("cur = ",cur)
                res.append(cur)

            return
        
        for i in range(0,n):
            # we generate new cur by slicing
            # [start:i+1] s1
            # . s2 
            # [i+1:end+1] s3
            # call the recursion again
            temp = ""
            if len(cur) == 0:
                temp = cur+string[0:i+1]
            else:
                temp = cur + "."+string[0:i+1]
            
            if i+1<=n-1:
                self.generate_all_ips_by_validating(string[i+1:],res,temp)
            else:
                self.generate_all_ips_by_validating("",res,temp)



    def restoreIpAddresses(self, string):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(string)

        cur = ""
        self.generate_all_ips_by_validating(string,res,cur)
        return res
