class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.append(len([j for j in nums if j < i]))
        
        return ans
