class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        for i in range(len(nums) - 1):
            if nums[i] not in arr and nums[i] == nums[i + 1]:
                arr.append(nums[i])
            if len(arr) == 2:
                break
        return arr