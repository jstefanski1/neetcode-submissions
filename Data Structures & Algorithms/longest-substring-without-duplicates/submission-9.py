class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        maxL = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            maxL = max(maxL, r - l + 1)
            mp[s[r]] = r
        return maxL