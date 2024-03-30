class Solution(object):

    def find_xor_in_range(self,arr,left,right):
        xor = 0
        for i in range(left,right+1):
            xor = (xor ^ arr[i])%1

        return xor

    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []

        n = len(arr)

        prefix_xor = []
        prefix_xor.append(arr[0])

        for i in range(1,n):
            prefix_xor.append(prefix_xor[i-1] ^ arr[i])


        for query in queries:
            left = query[0]
            right = query[1]

            if left == 0:
                temp = prefix_xor[right]
            else:
                temp = prefix_xor[right] ^ prefix_xor[left-1]

            res.append(temp)

        return res
        