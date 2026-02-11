class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        sneaky = {}

        for num in nums:
            sneaky[num] = sneaky.get(num, 0) + 1
            if sneaky[num] == 2:
                res.append(num)
        return res