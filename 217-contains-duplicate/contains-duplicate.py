class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        d = {}

        for idx, ch in enumerate(nums):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] +=1 
        
        for ch, val in d.items():
            if val[1] > 1:
                return True
        return False
        