class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        no_of_peope_alive = [0 for i in range(2051)]

        for log in logs:
            no_of_peope_alive[log[0]]+= 1
            no_of_peope_alive[log[1]]-= 1

        max_value = -1
        year = 0
        for i in range(1950,2051):
            no_of_peope_alive[i] =no_of_peope_alive[i-1]+no_of_peope_alive[i] 
            if max_value<no_of_peope_alive[i]:
                max_value = no_of_peope_alive[i]
                year = i
            
        return year
        