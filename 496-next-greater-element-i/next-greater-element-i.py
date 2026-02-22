class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        # Try to traverse elements from the nums2 in reverse order
        n = len(nums2)

        nge = dict()

        for i in range(n-1,-1,-1):

            while len(stack)>0 and stack[len(stack)-1]<=nums2[i]:
                stack.pop(len(stack)-1)
            
            if len(stack)==0:
                nge[nums2[i]] = -1
            else:
                nge[nums2[i]] = stack[len(stack)-1]
            
            stack.append(nums2[i])
        
        res = []
        for ele in nums1:
            res.append(nge[ele])
        return res

            

