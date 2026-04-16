class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n):
            target = -nums[i]

            hmap = {}
            for j in range(i + 1, n):
                remainder = target - nums[j]

                if remainder in hmap:
                    result.add((nums[i], remainder, nums[j]))
                
                hmap[nums[j]] = j

        return [list(i) for i in result]