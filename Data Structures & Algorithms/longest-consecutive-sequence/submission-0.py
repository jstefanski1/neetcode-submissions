class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in nums:
            if n-1 not in s:
                count = 1
                while n + count in s:
                    count += 1
                res = max(res, count)
        return res

                