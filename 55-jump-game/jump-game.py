class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        i = n-2

        if n == 1:
            return True
        
        while(i>=0 and target!=0):
            if (nums[i] >= target-i):
                target = i
                i-=1
            else:
                while (nums[i] < (target-i)):
                    i-=1
                    if i<0:
                        return False
        
        if target<=0:
            return True


