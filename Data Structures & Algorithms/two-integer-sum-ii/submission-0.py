class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(numbers)):
            remainder = target - numbers[i]

            if remainder in hmap:
                return [hmap[remainder], i + 1]
            
            hmap[numbers[i]] = i + 1