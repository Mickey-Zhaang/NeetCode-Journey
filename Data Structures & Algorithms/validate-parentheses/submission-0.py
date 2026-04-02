class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closedToOpen:
                if stack and stakc[-1] == closedTopOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


