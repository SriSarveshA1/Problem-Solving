import math
import heapq

class Solution:
    def return_dis_between_two_points(self,x2,y2):
        part1 = (-x2)**2
        part2 = (-y2)**2
        return math.sqrt(part1+part2)

    def heap_push(self,hp,priority_value,add_value):
        heapq.heappush(hp,(-priority_value,add_value))
    
    def heap_pop(self,hp):
        return heapq.heappop(hp)



    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We maintain min-heap of size k.
        hp = []
        heapq.heapify(hp)

        for point in points:
            # we iterate each point 
            # 1. compute its distance between (0,0) and (point[0],point[1])
            # 2. Store the computed distance along with the heap
            # 3. If the computed distance is larger than the current min element of the heap we skip it
            # 4. Or else we add it to the heap, if the heap size is >k we remove the first element

            computed_dis = self.return_dis_between_two_points(point[0],point[1])

            if len(hp)==k:
                priority_value_of_top_node,points_arr = hp[0]
                if -priority_value_of_top_node < computed_dis:
                    continue
            
            self.heap_push(hp,computed_dis,[point[0],point[1]])

            if len(hp)>k:
                self.heap_pop(hp)
            

        res = []
        for ele in hp:
            v,k = ele
            res.append(k)
        return res
            

            

