class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, cnt in count.items():
            freq[cnt].append(n)
        soln = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                if n not in soln:
                    soln.append(n)
                if len(soln) == k:
                    return soln