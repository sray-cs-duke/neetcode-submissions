class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        for x in num_set:
            if x-1 not in num_set:
                length = 1
                while x + length in num_set:
                    length += 1

                longest = max(0, length)
        return longest