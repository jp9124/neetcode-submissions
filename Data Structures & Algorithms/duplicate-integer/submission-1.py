class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for x in nums:
            if x in nums_set:
                return True
            else:
                nums_set.add(x)
        return False

