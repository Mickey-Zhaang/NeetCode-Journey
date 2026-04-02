class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > nums[r]:
                # left side
                if target > nums[m] or target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[l]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
