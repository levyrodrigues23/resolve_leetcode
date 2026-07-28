class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_d = {}
        most_freq = {}
        lista = []

        for ch in nums:
            if ch not in freq_d:
                freq_d[ch] = 1
            else:
                freq_d[ch] += 1

        
        ordenado = sorted(freq_d.items(), key=lambda item: item[1], reverse=True)

            
            
        for ch in ordenado[:k]:
            lista.append(ch[0])

        return lista



           

     

        