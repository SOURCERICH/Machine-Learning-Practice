class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        return binary_search(0, len(nums) - 1)
