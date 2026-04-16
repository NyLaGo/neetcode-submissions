class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        left = 0
        right = n * m - 1

        while left <= right:
            mid = left + (right - left)//2

            x, y = mid % m, mid // m

            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False