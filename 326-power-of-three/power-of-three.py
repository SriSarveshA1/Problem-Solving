import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        value = round(math.log(n,3) / math.log(3,3))

        return math.pow(3,value) == n