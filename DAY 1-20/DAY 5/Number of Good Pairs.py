class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        x = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if (nums[i] == nums[j]) and (i < j):
                    x += 1
        return x