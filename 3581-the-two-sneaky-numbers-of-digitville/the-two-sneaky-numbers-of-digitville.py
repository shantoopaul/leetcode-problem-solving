class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        for i in range(len(nums) - 1):
            if not nums[i] in arr and nums[i] == nums[i + 1]:
                arr.append(nums[i])
        return arr