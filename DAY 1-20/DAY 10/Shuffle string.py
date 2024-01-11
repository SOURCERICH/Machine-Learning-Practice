class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
                ans += s[indices.index(i)]
        return ans