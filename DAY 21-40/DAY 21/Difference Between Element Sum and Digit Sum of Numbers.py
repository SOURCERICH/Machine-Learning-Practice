class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ans = map(int, list("".join(map(str, nums))))
        return abs(sum(nums) - sum(ans))