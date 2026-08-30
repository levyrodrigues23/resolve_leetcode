class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, 0 

        while l <= len(haystack) - len(needle):
            r = 0

            while r < len(needle) and haystack[l + r] == needle[r]:
                r += 1



            if r >= len(needle):
                return l

            l += 1

        return - 1


      




        