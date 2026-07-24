class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maior_area = 0
        


        while l < r:
            area = (r-l) * min(height[r],height[l])


            maior_area = max(maior_area, area)
            

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return maior_area


        