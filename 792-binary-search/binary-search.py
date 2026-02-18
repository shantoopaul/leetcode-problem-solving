class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        while a <= b:
            k = (a + b) // 2
            if (nums[k] == target):
                return k
            if nums[k] < target:
                a = k + 1
            else:
                b = k - 1
        return -1