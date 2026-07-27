class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d_s = {}
        d_t = {}

        for ch in s:
            d_s[ch] = d_s.get(ch, 0) +1

        for ch in t:
            d_t[ch] = d_t.get(ch, 0) +1

        return d_s == d_t 
             



        


        