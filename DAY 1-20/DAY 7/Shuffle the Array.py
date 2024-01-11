class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        nums2 = []
        i = 0
        for i in range(n):
            j = i + n
            nums2.append(nums[i])
            nums2.append(nums[j])

        nums = nums2
        return nums
        
