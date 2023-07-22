class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hesh = {}
        for i, val in enumerate(nums):
            if val in hesh:
                return val
            else:
                hesh[val] = 1