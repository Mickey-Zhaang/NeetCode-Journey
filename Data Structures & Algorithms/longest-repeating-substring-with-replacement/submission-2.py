class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        n = len(s)
        seen = {}
        long_char = ""

        l,r = 0, 0

        while r < n:
            cur = s[l:r+1]

            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1
            long_char = s[r] if seen[s[r]] == max(seen.values()) else long_char
            cur_longest = len(cur) - seen[long_char]
            if cur_longest > k:
                while s[l] != s[r]:
                    seen[s[l]] -= 1
                    l += 1
            longest = max(longest, r - l + 1)
            r += 1

        
        return longest