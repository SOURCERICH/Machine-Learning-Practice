

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        if len(ans) > 1:
            for k in ans[0:-1]:
                if k != k[::-1]:
                    ans.remove(k)
                elif len(k) == 1:
                    ans.remove(k)
            print(ans)
            while len(ans) > 1:
                ans.remove(min(ans))
        return ans
s = "babad"
Solution.longestPalindrome(s,s)
