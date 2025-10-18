class Solution:
    def reverseString(self, s: List[str]) -> None:
        leftt, right = 0, len(s) - 1

        while leftt < right:
            s[leftt], s[right] = s[right], s[leftt]
            leftt += 1
            right -= 1

    


        