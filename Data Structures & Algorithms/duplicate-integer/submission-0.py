class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for i in nums:
            values.add(i)
        if len(nums) != len(values):
            return True
        return False

        