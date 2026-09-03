class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            abc = [0] * 26
            for c in s:
                abc[ord(c) - ord('a')] += 1
            m[tuple(abc)].append(s)
        return list(m.values())
