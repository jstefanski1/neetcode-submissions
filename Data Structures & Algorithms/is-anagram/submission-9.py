class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        sM, tM = {}, {}
        
        for i in range(len(s)):
            sM[s[i]] = 1 + sM.get(s[i], 0)
            tM[t[i]] = 1 + tM.get(t[i], 0)
        
        return sM == tM