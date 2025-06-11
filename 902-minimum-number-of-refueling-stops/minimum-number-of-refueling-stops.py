from heapq import heappop, heappush, heapify

class Solution:

    def move_cur_l_pointer_return(self, l, stations, max_heap, cur_pos):
        n = len(stations)
        while (l+1<n and cur_pos>=stations[l+1][0]):
            heappush(max_heap,-1 * stations[l+1][1])
            l = l+1
        
        return l


    def minRefuelStops(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        heapify(max_heap)
        
        if target - start_fuel == 0:
            return 0
        
        cur_pos = 0

        no_of_stops = 0

        cur_fuel = start_fuel

        l = -1

        while cur_pos < target:
            cur_pos += cur_fuel 

            if cur_pos >= target:
                print(max_heap)

                return no_of_stops
            elif cur_pos < target:
                cur_fuel = 0


                l = self.move_cur_l_pointer_return(l,stations,max_heap,cur_pos)
                
                if len(max_heap) == 0:
                    return -1

                cur_fuel += (-1 * heappop(max_heap))
                no_of_stops+=1
        print(max_heap)
        return no_of_stops






