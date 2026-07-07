class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target-nums[i]
            nnums = nums[(i+1):]
            if diff in nnums:
                return [i, i+1+nnums.index(diff)]