class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        biggest_num = max(nums)
        x = nums.index(biggest_num)
        for num in nums:
            if num*2 > biggest_num and num != biggest_num:
                return -1
        return x
        