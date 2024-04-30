class Solution:

    def get_adjacent_groups(self,arr,no_adj_flowers,wait_day):
        
        n = len(arr)
        
        groups=0

        i = 0

        while (i<n):
            
            count = 0
            while(i<n and arr[i]<=wait_day):
                count+=1
                i+=1
            
            groups+=int(count/no_adj_flowers)
            i+=1
            
        return groups

        

    def minDays(self, arr: List[int], no_of_botiques: int, no_adj_flowers: int) -> int:
        
        if (no_of_botiques*no_adj_flowers) > len(arr):
            return -1 
        
        low = min(arr)
        high = max(arr)

        ans = -1 
        while(low<=high):
            mid = int((low+high)/2)

            print("for mid = ",mid," ",self.get_adjacent_groups(arr,no_adj_flowers,mid))
            if self.get_adjacent_groups(arr,no_adj_flowers,mid)>=no_of_botiques:
                ans = mid
                high = mid-1
                
            else:
                low = mid+1

        return ans