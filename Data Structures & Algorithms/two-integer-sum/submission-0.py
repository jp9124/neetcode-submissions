class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #diff = potential difference -> where it is in nums
        diff = {}
        for x in range(len(nums)):
            print(nums[x], diff)
            if target-nums[x] in diff:
                return [diff[target-nums[x]], x]
            else:
                diff[nums[x]] = x
        