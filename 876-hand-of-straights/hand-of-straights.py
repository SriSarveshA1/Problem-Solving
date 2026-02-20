import heapq

class Solution:
    def isNStraightHand(self, arr: List[int], groupSize: int) -> bool:
        n = len(arr)

        if (n%groupSize) != 0:
            return False
        
        res = []

        freq_map = dict()
        for ele in arr:
            if ele in freq_map:
                freq_map[ele] +=1
            else:
                freq_map[ele] = 1

        pq = []
        for ele,freq in freq_map.items():
            heapq.heappush(pq,(ele,freq))

        # print("pq = ",pq)

        while(len(pq)!=0):
            # Retrieve the groupSize no of elements from the pq and insert into cur,
            cur = []
            for i in range(0,groupSize):
                if len(pq)==0:
                    return False

                poped_ele,poped_freq = heapq.heappop(pq)

                # print("...cur = ",cur)
                # print("poped_ele, poped_freq = ",poped_ele, poped_freq)

                if len(cur)>0 and cur[len(cur)-1]+1 != poped_ele:
                    return False

                cur.append(poped_ele)
            
            # print("cur after ",cur)
            
            # Then iterate the cur, and pick the elements and reduce its freq by 1 and then insert back to pq
            for ele in cur:
                # Get the freq of ele from freq_map and reduce it by 1
                freq_of_ele = freq_map[ele]
                freq_of_ele = freq_of_ele - 1
                freq_map[ele] = freq_of_ele

                if freq_of_ele > 0:
                    heapq.heappush(pq,(ele,freq_of_ele))
            
            res.append(cur)
        
        # print("res = ",res)
        if len(res) == (n/groupSize):
            return True
        
        return False


        

