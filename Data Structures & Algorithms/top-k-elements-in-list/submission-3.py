class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cm = {}
        freq = [[] for n in range(len(nums)+1)]

        for n in nums:
            cm[n] = 1 + cm.get(n, 0)
        for n,c in cm.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res