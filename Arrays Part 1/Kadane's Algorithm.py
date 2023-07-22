class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currentSum = float('-inf'),0
        for i in range(len(nums)):
            currentSum += nums[i]
            maxSum = max(currentSum, maxSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum
