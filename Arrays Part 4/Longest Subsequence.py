class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        count = 1
        curr = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                curr += 1
            else:
                curr = 1
            if curr > count:
                count = curr
        return count if nums != [] else 0