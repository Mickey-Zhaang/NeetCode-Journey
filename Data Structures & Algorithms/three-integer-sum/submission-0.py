class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        result = []
        
        sec_last = len(nums) - 1
        
        if nums[0] > 0: return
        
        for i in range(sec_last):
            target = nums[i]
            l, r = i + 1, sec_last
            while l < r:
                if nums[l] + nums[r] + target == 0:
                    result.append([nums[l], nums[r], target])
                l += 1
                r -= 1
        return result