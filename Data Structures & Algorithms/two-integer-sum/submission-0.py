class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for x in nums:
            needed = target - x
        
        for i, x in enumerate(nums):
            if needed in seen:
                return [seen[needed], i]

        seen[x] = i
        

        
        
