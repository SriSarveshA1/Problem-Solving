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
        costs.sort(key=cmp_to_key(self.compare_func))

        print("///",costs)

        n = len(costs)
        A = n/2
        B = n/2

        idx = n-1

        total = 0

        while idx>=0:
            cost_of_city_a = costs[idx][0]
            cost_of_city_b = costs[idx][1]

            if  cost_of_city_a < cost_of_city_b:
                if A>=1:
                    A-=1
                    total+=cost_of_city_a
                elif B>=1:
                    B-=1
                    total+=cost_of_city_b
            else:
                if B>=1:
                    B-=1
                    total+=cost_of_city_b
                elif A>=1:
                    A-=1
                    total+=cost_of_city_a
            
            idx-=1

        return total
        

        