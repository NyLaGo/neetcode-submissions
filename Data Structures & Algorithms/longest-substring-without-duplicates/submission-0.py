class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hmap = {}

        result = 0
        while r < len(s):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
              
            while hmap[s[r]] > 1:
                hmap[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
            r += 1

        return result