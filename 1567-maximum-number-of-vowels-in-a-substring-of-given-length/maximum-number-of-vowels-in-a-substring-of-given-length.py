class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        window_vowels = 0
        max_vowels = 0
        vogais = {"a", "e", "i", "o", "u"}

        for r in range(len(s)):
            if s[r] in vogais:
                window_vowels += 1

            if r - l + 1 == k:
                max_vowels = max(max_vowels, window_vowels)

                if s[l] in vogais:
                    window_vowels -= 1

                l += 1

        return max_vowels