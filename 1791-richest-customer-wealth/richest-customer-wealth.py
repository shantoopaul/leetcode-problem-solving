class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for acc in accounts:
            res.append(sum(acc))
        return max(res)