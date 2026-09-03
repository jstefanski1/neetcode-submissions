class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        m = {}
        l = 0
        
        for r in range(len(s)):
            if s[r] in m:
                l = max(l, m[s[r]] + 1)
            m[s[r]] = r
            maxL = max(maxL, r - l + 1)
        return maxL