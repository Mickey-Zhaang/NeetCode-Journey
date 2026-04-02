class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                # m is in left sorted => look right
                l = m + 1
            else:
                # m is in right sorted => look left
                r = m
        return nums[l]

