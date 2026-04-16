class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []

        left = [0] * n
        right = [0] * n


        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop(-1)
            
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            
            stack.append(i)
        
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop(-1)
            
            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1]
            
            stack.append(i)
        
        stack.clear()

        rect = 0

        for i in range(n):
            rect = max(rect, heights[i] * (right[i] - left[i] -1))

        return rect