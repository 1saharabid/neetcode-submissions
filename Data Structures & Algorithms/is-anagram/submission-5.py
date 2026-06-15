class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val = False
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            val = True
        return val
        