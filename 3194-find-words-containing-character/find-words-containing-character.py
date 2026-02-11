class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, n in enumerate(words) if x in n]