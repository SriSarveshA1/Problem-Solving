class Solution:
    def minRefuelStops(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        if start_fuel >= target:
            return 0

        max_heap = []
        i, n = 0, len(stations)
        stops = 0
        max_distance = start_fuel

        while max_distance < target:
            if i < n and stations[i][0] <= max_distance:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            elif not max_heap:
                return -1
            else:
                max_distance += -heapq.heappop(max_heap)
                stops += 1

        return stops