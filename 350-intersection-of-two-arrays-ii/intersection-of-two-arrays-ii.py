class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n1 = len(nums1)

        nums2.sort()
        n2 = len(nums2)

        i=0
        j=0

        res = []

        while(i<n1 and j<n2):
            if(nums1[i] < nums2[j]):
                i+=1
            else:
                if(nums1[i]>nums2[j]):
                    j+=1
                else:
                    res.append(nums1[i])

                    i+=1
                    j+=1
        
        return res