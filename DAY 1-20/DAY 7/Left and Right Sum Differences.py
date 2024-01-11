class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        leftSum = [] * n
        rightSum = [] * n

        for i in range(len(nums)):
            leftSum.append(sum([nums[x] for x in range(len(nums)) if x < i]))
            rightSum.append(sum([nums[x] for x in range(len(nums)) if x > i]))

        for i in range(len(answer)):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer