class Solution:

    def get_mid(self,low,high):
        if(low+high+1)%2 == 0:
            return int(low+((high-low)/2))

        return int(low+((high-low+1)/2))

    def singleNonDuplicate(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        if n == 1:
            return arr[0]
        
        l = 0
        r = n-1

        while(l<=r):
            mid = self.get_mid(l,r)

            if (
                (mid == 0 and arr[mid]!=arr[mid+1])
                or
                (mid == n-1 and arr[mid]!=arr[mid-1])
                or
                (arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1])
    
                ):
                return arr[mid]
            
            else:
                if ( 
                    ((arr[mid] == arr[mid-1]) and (mid+1)%2 == 0)
                    or
                    ((arr[mid] == arr[mid+1]) and (mid+1)%2 != 0)
                ):
                    l = mid+1
                else:
                    r = mid-1
        
        return -1
