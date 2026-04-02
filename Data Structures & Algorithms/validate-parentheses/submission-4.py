class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False

        seen = []

        fwd_brackets = { ")": "(", "]": "[", "}": "{"}


        for i in range(len(s)):
            cur = s[i]

            if cur not in fwd_brackets:
                seen.append(cur)
            else:
                last = seen.pop()

                if last != fwd_brackets[cur]:
                    return False
        
        return True
        

