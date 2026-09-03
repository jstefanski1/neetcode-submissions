class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        l = 0
        hm = {}

        for r in range(len(s)):
            if s[r] in hm:
                l = max(l, hm[s[r]] + 1)
            maxL = max(maxL, r-l + 1)
            hm[s[r]] = r
        return maxL