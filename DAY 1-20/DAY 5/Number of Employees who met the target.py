class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        j = 0
        for i in hours:
            if i >= target:
                j += 1 
        return j
