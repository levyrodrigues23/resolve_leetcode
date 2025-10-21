class Solution:
    def countBits(self, n: int) -> List[int]:
        lista_binarios = []
        for i in range(0, n + 1):
            binario = bin(i)[2::]
            quantidade = binario.count('1')
            lista_binarios.append(quantidade)

        return lista_binarios
        
            
            



        