class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            current = nums[i]
            diff = target-nums[i]
            if diff in indexes.keys():
                return [indexes[diff], i]
            indexes[current] = i