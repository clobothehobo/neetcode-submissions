class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodupes = set()
        for n in nums:
            if n in nodupes:
                return True
            else:
                nodupes.add(n)
        return False 
