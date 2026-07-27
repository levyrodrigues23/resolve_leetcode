class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}


        for idx, ch in enumerate(s):
            if ch not in hash_s:
                hash_s[ch] = t[idx]
            else:
                if hash_s[ch] != t[idx]:
                    return False

        for idx, ch in enumerate(t):
            if ch not in hash_t:
                hash_t[ch] = s[idx]
            else:
                if hash_t[ch] != s[idx]:
                    return False

        return True
        


        
                



        
        