class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = []
        for sentence in sentences:
            res.append(len(sentence.split()))
        return max(res)