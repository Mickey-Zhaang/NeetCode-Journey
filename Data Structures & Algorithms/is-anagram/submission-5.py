class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0] * 26

        for i, j in zip(s, t):
            seen[ord('a') - ord(i)] += 1
            seen[ord('a') - ord(j)] -= 1
        
        for i in seen:
            if i != 0:
                return False
        
        return True