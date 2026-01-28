import heapq


class Solution:
    def push(self,pq,ele):
        heapq.heappush(pq,-ele)

    def pop(self,pq):
        return -heapq.heappop(pq)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            self.push(pq,num)
        
        ans = None
        for i in range(1,k+1):
            ans = self.pop(pq)
        
        return ans
        