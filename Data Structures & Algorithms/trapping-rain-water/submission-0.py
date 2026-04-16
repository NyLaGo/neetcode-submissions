class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and height[i] >= stack[-1]:
                stack.pop(-1)
            
            stack.append(height[i])
            left[i] = stack[0]

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and height[i] >= stack[-1]:
                stack.pop(-1)
            
            stack.append(height[i])
            right[i] = stack[0]

        result = 0

        for i in range(n):
            result += min(left[i], right[i]) - height[i]

        return result