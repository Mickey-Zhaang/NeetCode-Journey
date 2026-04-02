class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        n = len(s)

        longest = 0

        l,r = 0,0

        while r < n:

            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1

            char_longest = max(seen.values())

            while r-l+1 - char_longest > k:
                if s[l] != s[r]:
                    seen[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r+=1
        
        return longest

