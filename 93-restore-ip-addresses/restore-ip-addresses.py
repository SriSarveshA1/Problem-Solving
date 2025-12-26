class Solution:
    def validate_ip_part(self,string):
        # 1.CHeck for trailing zeros
        # 2. ANd check for the ip part range
        int_value = int(string)
        str_value_of_int = str(int_value)

        if len(str_value_of_int) != len(string):
            #Trailing zero's present
            return False
        
        if int_value>=0 and int_value<=255:
            return True
        
        return False
    def validate_whole_ip_address(self,cur)->(bool,str):
        if len(cur)!=4:
            # No of parts is not equal to 4
            return False,""
        
        return True, ".".join(cur)
    def generateIpAddresses(self,cur,res,start,s,n):
        if start>=n:
            # If we reach the terminal
            # we validate the current cur and add it to result
            validation_result,string = self.validate_whole_ip_address(cur)
            if validation_result:
                res.append(string)
            
            return
        
        if len(cur)>4: #if the length of the parts has gone beyond 4 ,evn though still we havn't finished exploring the end of the string
            return 

        for i in range(start,n):

            if ((i+1) - start)+1 >4:# We do this because if we are in path where we are considering a substring which beyond the valid ip length
                break               # we break that path, as it won't give valid results

            if self.validate_ip_part(s[start:i+1]):
                cur.append(s[start:i+1])
                self.generateIpAddresses(cur,res,i+1,s,n)
                cur.pop()
    def restoreIpAddresses(self, s: str) -> List[str]:
        cur = []
        res = []
        n = len(s)
        self.generateIpAddresses(cur,res,0,s,n)
        return res
