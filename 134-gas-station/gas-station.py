import math

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        if n==1:
            return -1 if gas[0] < cost[0] else 0

        sum_of_gas = sum(gas)
        sum_of_cost = sum(cost)

        if sum_of_gas<sum_of_cost:
            return -1
        
        current_idx = 0
        current_count = 0
        current_gas = 0

        result_idx = -1


        while True:

            if current_count == n:
                result_idx = current_idx
                break
            
            current_gas += gas[current_idx] - cost[current_idx]

            if current_gas < 0:
                current_gas = 0
                current_count = 0
            else:
                #moving to next idx
                current_count += 1
            current_idx = int((current_idx + 1)%n)


        return result_idx




