class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        least = nums[0]
        for i in nums:
            if i < least:
                least = i
        return least