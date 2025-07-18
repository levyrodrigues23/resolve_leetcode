class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reverse = x_str[::-1]
        return reverse == x_str
        if reverse == x:
            return True
        else:
            return False



        