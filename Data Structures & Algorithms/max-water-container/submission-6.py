class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            maximum = max(maximum, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum