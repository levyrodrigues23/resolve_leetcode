class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        _hash = {}

        for ch in s:
            if ch not in _hash:
                _hash[ch] = 1
            else:
                _hash[ch] += 1

        for ch in t:
            if ch not in _hash or _hash[ch] == 0:
                return ch
            _hash[ch] -= 1
              


        

        

        
        