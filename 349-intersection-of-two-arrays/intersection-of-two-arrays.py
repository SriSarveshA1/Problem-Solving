class Solution(object):

    def find_existence(self,arr,key):
        low = 0
        high = len(arr)-1

        while(low<=high):
            mid = (low+high)/2
            if arr[mid] == key:
                return True
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_length = len(nums1)
        nums2_length = len(nums2)

        res = set()

        if(nums1_length<nums2_length):
            nums1.sort()
            for ele in nums2:
                if(self.find_existence(nums1,ele)):
                    res.add(ele)

        else:
            nums2.sort()
            for ele in nums1:
                if(self.find_existence(nums2,ele)):
                    res.add(ele)

        return res