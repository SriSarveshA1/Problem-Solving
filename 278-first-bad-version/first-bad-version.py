# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def find_mid(self,low,high):
        if((low+high+1)%2 == 0):
            return int(low+((high-low)/2))

        return int(low+((high-low+1)/2))

    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        ans = -1

        while (low<=high):
            mid = self.find_mid(low,high)
            print("l = ",low," r = ",high," mid = ",mid)
            if isBadVersion(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans