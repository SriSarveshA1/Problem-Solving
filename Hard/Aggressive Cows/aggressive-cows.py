#User function Template for python3

class Solution:
    
    def is_all_cows_placed(self,min_distance,nums,k):
        no_of_cows_placed = 1
        
        last_position = nums[0]
        
        for i in range(1,len(nums)):
            
            if(nums[i]-last_position>=min_distance):
                no_of_cows_placed+=1
                last_position = nums[i] 
                
            if(no_of_cows_placed == k):
                return True
        
        return False
    
    def solve(self,n,k,nums):

        nums.sort()
        
        n = len(nums)
        
        min_value = nums[0]
        max_value = nums[n-1]
        
        low = 1
        high = max_value-min_value
        
        while(low<=high):
            mid = int((low+high)/2)
            
            if(self.is_all_cows_placed(mid,nums,k) == False):
                high = mid-1
            else:
                ans = mid
                low = mid+1
            
        return ans
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends