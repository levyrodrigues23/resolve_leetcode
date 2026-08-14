class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _hash = {}
        result = []


        for ch in nums:
            if ch not in _hash:
                _hash[ch] = 1
            else:
                _hash[ch] += 1

        for ch in range(1, len(nums)+1):
            if ch not in _hash:
                result.append(ch)

        return result

        