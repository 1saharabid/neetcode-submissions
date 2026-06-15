class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val = True
        if len(s) != len(t):
            return False
        s_letters = set()
        for char in s:
            s_letters.add(char)
        print(s_letters)
        for char in t:
            if char in s_letters:
                val = True
                s_letters.remove(char)
            else:
                val = False
        if len(s_letters) > 0:
            val = False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            val = True
        return val
        