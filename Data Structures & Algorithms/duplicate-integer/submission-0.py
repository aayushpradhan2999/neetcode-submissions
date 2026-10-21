class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = set(nums)

        if len(unq) == len(nums):
            return False
        else:
            return True