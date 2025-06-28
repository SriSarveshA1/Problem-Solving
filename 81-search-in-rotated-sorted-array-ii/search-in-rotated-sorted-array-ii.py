class Solution:
    def get_mid(self,low,high):

        if (low+high+1)%2 == 0:
            return int(low+((high-low)/2))

        return int(low+((high-low+1)/2))

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = self.get_mid(l,r)

            print("l = ",l," r = ",r, " mid = ",mid)

            if (nums[mid]==target):
                return True 

            while (nums[l] == nums[r] and nums[l] != target):
                l = l+1
                r = r-1
                if l>r:
                    break
            
            if l>r:
                break
            
            if (nums[l]<=nums[mid]):
                # left side is sorted
                if nums[l]<=target and target<=nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            else:
                if nums[mid]<=target and target<=nums[r]:
                    l = mid + 1
                else:
                    r = mid -1

        return False


        