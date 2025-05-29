class Solution:
    def numRescueBoats(self, arr: List[int], limit: int) -> int:
        n = len(arr)

        arr = sorted(arr)
        l = 0
        r = n-1
        no_of_boats = 0

        while l<=r:
            current_boat_weight = arr[l] + arr[r]

            if current_boat_weight>limit:
                no_of_boats+=1
                r-=1
            else:
                l+=1
                r-=1
                no_of_boats+=1
            
        
        return no_of_boats