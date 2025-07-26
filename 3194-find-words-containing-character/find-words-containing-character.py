class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i, elemento in enumerate(words):
            if x in elemento:
                indices.append(i)
        return indices 