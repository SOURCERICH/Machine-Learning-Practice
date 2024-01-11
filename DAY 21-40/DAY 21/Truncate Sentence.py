s = "Hello how are you Contestant"
k = 4

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(map(str,words[:k]))
    
a = Solution()
print(a.truncateSentence(s,k))

