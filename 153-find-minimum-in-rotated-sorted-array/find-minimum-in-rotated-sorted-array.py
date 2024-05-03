class Solution:
    def find_mid(self,low ,high):
        if (low+high+1)%2 == 0:
            return int(low+(high-low)/2)

        return int(low+(high-low+1)/2)

    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n-1

        while(l<=r):
            mid = self.find_mid(l,r)

            if arr[l]<=arr[mid] and arr[mid]<=arr[r]:
                return arr[l]
            
            if arr[l]<=arr[mid] and arr[l]>arr[r]:
                l = mid+1
            else:
                r = mid 
        
        
