class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        temp = num

        num = str(num)

        n = len(num)

        if n<k:
            return 0


        l = 0
        r = k-1

        count = 0 

        while r<n:
            divisor = int(num[l:r+1])
            print(divisor)
            if divisor!=0 and (temp%divisor)==0:
                count+=1


            l=l+1
            r=r+1

        return count        
            

































































        