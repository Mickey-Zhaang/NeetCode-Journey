class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        seen = set()

        if not s:
            return 0

        longest = 1

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[r])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l)
            r += 1
        return longest
            