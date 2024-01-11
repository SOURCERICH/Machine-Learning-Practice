class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_set = set()
        i = 0  # Pointer to iterate through the array
        
        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
                nums[i] = num
                i += 1
        
        return i

