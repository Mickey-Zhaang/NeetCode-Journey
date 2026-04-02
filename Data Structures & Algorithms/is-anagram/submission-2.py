class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1, seen2 = [0] * 26, [0] * 26

        for i, j in zip(s, t):
            seen1[ord(i) - ord('a')] += 1
            seen2[ord(j) - ord('a')] += 1

        return seen1 == seen2

