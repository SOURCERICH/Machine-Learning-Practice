class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        n = len(nums)
        runningSum = [] * n
        for i in range(n):
            if i == 0:
                runningSum.append(nums[0])
            else:
                runningSum.append(runningSum[i-1] + nums[i])
            
            i += 1
        return runningSum
