class Solution:
    def isValid(self, s: str) -> bool:
        hm = {']': '[', '}':'{', ')':'(' }
        stack = []

        for c in s:
            if c in hm:
                if stack and hm[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack 