class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        x = 0
        sublist = []
        while x < len(nums):
            for j in range(nums[x]):
                sublist.append(nums[x+1])
            x += 2
        return sublist
