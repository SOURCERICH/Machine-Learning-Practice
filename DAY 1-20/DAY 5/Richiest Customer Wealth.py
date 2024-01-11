class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sums =[]
        for i in accounts:
            sums.append(sum(i))
            j = max(sums)
        return j