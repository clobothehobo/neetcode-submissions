class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in dnums:
                return [dnums[diff], i]
            dnums[nums[i]] = i