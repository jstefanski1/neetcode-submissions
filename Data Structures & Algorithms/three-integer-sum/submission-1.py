class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r-= 1
                elif s < 0:
                    l +=1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r = len(nums) -1
        return res

