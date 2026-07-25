# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
     

        while lo < hi:

            mid = int((lo + hi)//2)

            res = isBadVersion(mid)

            if res:
       
                hi = mid
            else:
                lo = mid+1

        return hi    


        