class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map1 = dict()
        i=0
        n=len(nums)
        while i < n:
            if nums[i] not in map1.keys():
                map1[nums[i]]=[i]
            else:
                map1[nums[i]].append(i)
            i = i+1

        nums.sort()
        l=0
        r=n-1
        while(l<r):
            res = nums[l] + nums[r]
            if res == target:
                if len(map1[nums[l]])>=2:
                    return [ map1[nums[l]][0], map1[nums[l]][1] ]

                return [ map1[nums[l]][0], map1[nums[r]][0] ]
            else:
                if res<target:
                    l = l+1
                else:
                    r = r-1
