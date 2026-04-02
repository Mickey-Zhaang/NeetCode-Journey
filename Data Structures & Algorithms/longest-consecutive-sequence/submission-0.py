class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        if not nums:
            return 0

        for i in nums:
            seen.add(i)

        longest = 1
        curr_longest = 1
        seen = list(seen)
        last = seen[0]
        for i in range(1, len(seen)):
            if seen[i] != last + 1:
                curr_longest = 0
            else:
                curr_longest += 1
            longest = max(longest, curr_longest)
            last = seen[i]
        return longest
            


            