#User function Template for python3
class Solution:
    def twoOddNum(self, nums, N):
        # code here
        if len(nums)==2:
            return nums

        xor = 0

        for num in nums:
            xor=xor^num

        #print("xor= ",xor)

        right_most_set_bit = (~xor+1) & xor

        #print("right_most_set_bit= ",right_most_set_bit)
        res = [0,0]        
        for num in nums:

            cur_num = num&right_most_set_bit
            if cur_num == 0:
                res[0]^=num
            else:
                res[1]^=num
        
        temp = res[1]
        if res[1]>res[0]:
            res[1] = res[0]
            res[0] = temp
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends