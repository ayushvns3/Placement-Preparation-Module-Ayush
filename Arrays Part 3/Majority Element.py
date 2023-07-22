class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        arr = list(set(nums))
        for i in range(len(arr)):
            temp = nums.count(arr[i])
            if temp > n:
                return arr[i]