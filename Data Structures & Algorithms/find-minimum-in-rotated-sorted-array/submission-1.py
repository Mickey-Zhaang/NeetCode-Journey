class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            l_val, r_val = nums[l], nums[r]
            mid = int((r - l + 1) / 2)
            mid_val = nums[mid]

            if l_val < r_val:
                # sorted case
                r = mid
            else:
                if mid_val > l_val:
                    l = mid + 1
                else:
                    r = mid

        return nums[l]


