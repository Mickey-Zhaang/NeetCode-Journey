class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = set()
        seen2 = set()

        for i, j in zip(s, t):
            seen1.add(i)
            seen2.add(j)
        
        return seen1 == seen2

