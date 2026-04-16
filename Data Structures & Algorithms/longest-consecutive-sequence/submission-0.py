class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        result = 0

        for num in nums:
            if not hmap[num]:
                hmap[num] = hmap[num - 1] + hmap[num + 1] + 1
                hmap[num - hmap[num - 1 ]] = hmap[num]
                hmap[num + hmap[num + 1]] = hmap[num]
                result = max(result, hmap[num])
        
        return result
