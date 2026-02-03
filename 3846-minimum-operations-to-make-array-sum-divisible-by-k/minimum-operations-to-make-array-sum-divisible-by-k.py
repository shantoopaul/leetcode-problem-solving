class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for num in nums:
            total += num
        if total % k == 0:
            return 0
        else:
            return total % k

