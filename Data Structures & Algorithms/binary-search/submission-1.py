class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid = len(nums) / 2

        for x in nums:
            if x == target:
                return nums[x]
            
            elif x < target:
                mid += 1
            
            elif x > target:
                mid -= 1
            
            else:
                return -1
        