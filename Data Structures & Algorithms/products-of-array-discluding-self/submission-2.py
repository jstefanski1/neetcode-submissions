class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        lr = 1
        for i in range(len(nums)):
            res[i] = lr
            lr = lr * nums[i]
        rr = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= rr
            rr = nums[i] * rr
        return res