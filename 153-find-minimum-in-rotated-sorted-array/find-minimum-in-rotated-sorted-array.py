class Solution:
    def find_mid(self,low ,high):
        if (low+high+1)%2 == 0:
            return int(low+(high-low)/2)

        return int(low+(high-low+1)/2)

    def is_valid_mini(self,arr,mid):
        n = len(arr)
        if mid-1 < 0 and mid+1 <=n:
            return True
        
        if mid-1>=0 and arr[mid-1]>arr[mid]:
            return True

    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n-1

        while(l<=r):
            mid = self.find_mid(l,r)

            if l==r:
                return arr[mid]
            
            if mid-1 < 0 and arr[mid]<arr[mid+1]:
                return arr[mid]
            
            if mid-1 >= 0:
                if arr[mid-1]>arr[mid]:
                    return arr[mid]
                
            if arr[l] <= arr[mid]:
                if arr[l] <= arr[r]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if arr[mid] <= arr[r]:
                    r = mid-1
                else:
                    l = mid+1
        
            
            
            

        
        