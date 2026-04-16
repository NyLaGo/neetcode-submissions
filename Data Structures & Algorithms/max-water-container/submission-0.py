class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        volume = 0
        result = 0

        while left < right:
            if heights[left] < heights[right]:
                volume = max(volume, (right - left) * heights[left])
                left += 1
            else:
                volume = max(volume, (right - left) * heights[right])
                right -= 1

        return volume
                