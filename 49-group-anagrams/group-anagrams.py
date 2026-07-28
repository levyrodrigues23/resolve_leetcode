class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _hash = {}

        for ch in strs:
            chave = "".join(sorted(ch))

            if chave not in _hash:
                _hash[chave] = [ch]
            else:
                _hash[chave].append(ch)

        return list(_hash.values())