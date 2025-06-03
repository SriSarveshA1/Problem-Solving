from functools import cmp_to_key

class Solution:



    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by difference (NOT absolute difference)
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total = 0
        
        # First n people go to city A, rest go to city B
        for i in range(len(costs)):
            if i < n:
                total += costs[i][0]  # Send to city A
            else:
                total += costs[i][1]  # Send to city B
        
        return total