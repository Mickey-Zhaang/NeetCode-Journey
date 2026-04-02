class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("inf")

        have, need = 0, len(countT)

        l = 0

        for r in range(len(s)):
            curr = s[r]

            if curr in countT:
                window[curr] = 1 + window.get(curr, 0)
                if window[curr] >= countT[curr]:
                    have += 1
            while have == need:
                if s[l] in countT and window[s[l]] >= 1:
                    have -= 1
                if r - l + 1 < resLen:
                    res = [l, r]
                l += 1
                
        
        l, r = res

        return s[l:r + 1]
