class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = 0 
        prefix_xor = [ 0 for i in range(0,len(arr))]
        prefix_xor[0] = arr[0]
        for i in range(1,len(arr)):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i]

        result = []
        for query in queries:
            l = query[0]
            r = query[1]
            if l != 0:
                result.append(prefix_xor[r]^prefix_xor[l-1])
            else:
                result.append(prefix_xor[r])
        return result