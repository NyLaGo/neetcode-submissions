class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1
            counter_t[t[i]] = counter_t.get(t[i], 0) + 1

        for char in counter_s:
            if counter_s.get(char) != counter_t.get(char, 0):
                return False
        
        return True