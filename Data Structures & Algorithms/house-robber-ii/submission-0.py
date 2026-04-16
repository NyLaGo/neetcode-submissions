class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1 (nums):
            l = len(nums)

            if l == 1:
                return nums[0]
            
            dp = [0] * l

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, l):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
            return dp[-1]
        
        n = len(nums)

        if n == 1:
            return nums[0]

        return max(rob1(nums[:n - 1]), rob1(nums[1:]))