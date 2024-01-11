class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = set(range(1,len(nums)+1))
        return list(ans - set(nums))


        