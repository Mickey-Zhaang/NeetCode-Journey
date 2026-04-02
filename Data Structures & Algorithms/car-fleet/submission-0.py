class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vels = [(p, s) for p, s in zip(position, speed)]
        vels.sort()
        
        stack = []

        for i in range(len(vels) - 1, -1, -1):
            p, s = vels[i]
            time = (target - p) // s

            while stack and stack[-1] >= time:
                stack.pop()

            stack.append(time)
        
        return len(stack)

