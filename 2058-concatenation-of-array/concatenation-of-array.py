class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for elemento in nums:
            ans.append(elemento)

        return ans + nums
        