import heapq


class Solution:
    def push(self,pq,ele):
        # Trying to do min heap by adding the negative values
        heapq.heappush(pq,ele)

    def pop(self,pq):
        return heapq.heappop(pq)

    def peek(self,pq):
        return pq[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            #print(pq)
            if len(pq)==k and self.peek(pq) > num:
                continue

            self.push(pq,num)

            if len(pq)>k:
                self.pop(pq)
        
        return self.pop(pq)
        
       
        