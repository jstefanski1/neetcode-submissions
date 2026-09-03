class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =  [1] * len(nums)

        forward = 1
        for i in range(len(nums)):
            res[i] = forward
            forward *= nums[i]
        backwards = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= backwards
            backwards *= nums[i]
        return res


