class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        ans =[]
        for i in candies:
            if (i + extraCandies) >= m:
                ans.append(True)
            else:
                ans.append(False)
        return ans
