#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        temp = [0 for i in range(2361)]
        no_trains_at_time = [0 for i in range(2361)]
        
        min_time = 100000
        
        for i in range(0,len(arr)):
            temp[arr[i]] +=1
            temp[dep[i]+1] -=1
            min_time = min(arr[i],min_time)
        
        max_value = -1
        
        no_trains_at_time[min_time] = temp[min_time]

        for i in range(min_time+1,2360):
            no_trains_at_time[i] =no_trains_at_time[i-1]+temp[i] #prefix calculation
            if max_value<no_trains_at_time[i]:
                max_value = no_trains_at_time[i]
                
            
        return max_value
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends