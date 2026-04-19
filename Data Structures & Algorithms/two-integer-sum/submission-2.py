class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for num in range(len(nums)):
            for nextNum in range(num+1, len(nums)):
                if nums[num]+nums[nextNum] == target:
                    result.append(num)
                    result.append(nextNum)
                    return result

            