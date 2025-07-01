import math 

class Solution:
    def find_mid(self,low,high):
        if (high-low)%2 == 0:
            return int(low+(high-low)/2)
        return int(low+(high-low+1)/2)

    def check_and_return_no_of_hours(self,arr,k) -> (bool,int):
        
        no_of_hours = 0
        for ele in arr:
            if (ele/k) == 1 or ele <= k:
                no_of_hours +=1
                continue
            else:
                no_of_hours += math.floor((ele/k))
                if (ele%k)>0:
                    no_of_hours += 1


        
        return no_of_hours


    def minEatingSpeed(self, arr: List[int], h: int) -> int:

        low = 1
        high = max(arr)
        ans = -1

        arr = sorted(arr)

        while (low<=high):
            mid = self.find_mid(low,high)
            print("mid = ",mid)
            print("hours = ",self.check_and_return_no_of_hours(arr,mid))
            if self.check_and_return_no_of_hours(arr,mid) <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans

