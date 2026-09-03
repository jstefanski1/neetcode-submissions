class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # returning indicies
        # target number to achieve
        # soln: map {key: num, value: indice}

        hMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hMap:
                return [hMap[diff], i]
            hMap[n] = i