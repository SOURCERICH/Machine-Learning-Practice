class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [] * n
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
            print(prefix[i])
        for i in reversed(range(n-1)):
            suffix[i] = suffix[i+1] * nums[i+1]
            print(suffix[i])
        for i in range(n):
            x = prefix[i] * suffix[i]
            ans.append(x)
        return ans
