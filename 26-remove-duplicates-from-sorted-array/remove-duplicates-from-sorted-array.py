class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        k = 1

        while r < len(nums):
            if nums[r] == nums[l-1]:
                r+=1
            else:
                nums[l] = nums[r]
                k += 1
                l+=1 
                r+=1

        return k


        