class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maior = 0
        numeros = set(nums)


        for num in numeros:
            if num - 1 not in numeros:
                atual = num
                tamanho = 1


                while atual + 1 in numeros:
                    atual += 1
                    tamanho  += 1

                maior = max(maior, tamanho)

        return maior

            



       

        