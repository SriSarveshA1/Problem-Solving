from functools import cmp_to_key

class Solution:

    def compare_func(self,value_1,value_2):
        if abs(value_1[0]-value_1[1]) > abs(value_2[0]-value_2[1]):
            return 1
        elif abs(value_1[0]-value_1[1]) < abs(value_2[0]-value_2[1]):
            return -1
        else:
            return 0


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