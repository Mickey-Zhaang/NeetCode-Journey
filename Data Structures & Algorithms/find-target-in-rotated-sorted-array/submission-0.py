class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n

        while l < r:
            m = int(l + r) // 2
            

            # base case
            if nums[m] == target:
                return m
            
            # you are in left portion
            if nums[m] > nums[r]:
                if target > nums[m] or target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # you are in right portion
            else:
                if target < nums[m] or target > nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
