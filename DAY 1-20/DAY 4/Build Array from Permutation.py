
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        
        return ans
    

nums = [0, 2, 1, 5, 3, 4]
solution = Solution()
result = solution.buildArray(nums)
print(result)
