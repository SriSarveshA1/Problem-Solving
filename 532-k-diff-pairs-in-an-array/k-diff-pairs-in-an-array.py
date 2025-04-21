class Solution:

    def get_tuple(self, num1, num2):
        min_num = min(num1, num2)
        max_num = max(num1, num2)
        return (min_num, max_num)

    def findPairs(self, nums, k):
        # Code here
        freq_map = dict()
        count = 0
        set_ele = set()

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for num in nums:
            if k + num in freq_map and (self.get_tuple(num, k + num)) not in set_ele:
                if k + num == num and k == 0 and freq_map[num] < 2:
                    continue

                count += 1
                set_ele.add(self.get_tuple(num, k + num))

        return count

        