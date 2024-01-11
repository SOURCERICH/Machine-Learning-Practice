class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for i in range(len(nums1)+1):
            if i > m:
                nums1.pop()
        
        for j in nums2:
            nums1.append(j)
        
        nums1.sort()