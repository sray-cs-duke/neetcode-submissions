class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            least = nums[0]
            if nums[i] <= least:
                least = nums[i]
        return least