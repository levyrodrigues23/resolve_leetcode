from collections import Counter 

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)

        sorte_maxima = -1

        for num, freq in counter.items():
            if num == freq and num > sorte_maxima:
                sorte_maxima = num
            
        return sorte_maxima


        
        
        