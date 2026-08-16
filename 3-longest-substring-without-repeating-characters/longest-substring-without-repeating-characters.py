class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, l = 0, 0
        chars = set()
        maior = 0
        

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                maior = max(maior, r - l + 1)
                r+= 1

            else:
                chars.remove(s[l])
                l+= 1

        return maior



        