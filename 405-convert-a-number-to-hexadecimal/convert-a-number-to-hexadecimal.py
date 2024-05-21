class Solution(object):
    def toHex(self, n):
        """
        :type num: int
        :rtype: str
        """
        hash_map = dict()
        hash_map[10] = 'a'
        hash_map[11] = 'b'
        hash_map[12] = 'c'
        hash_map[13] = 'd'
        hash_map[14] = 'e'
        hash_map[15] = 'f'
        
        string = ""
        if n==0:
            return "0"
        
        if n<0: 
            n = pow(2,32)+n
        
        while(n!=0):
            rem = n%16
            if(rem<=9):
                string+=str(rem)
            else:
                string+=hash_map[rem]

         
            n = n/16
        
        return string[::-1]


        