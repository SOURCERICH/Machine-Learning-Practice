class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        n = len(encoded) + 1
        arr = [0] * (n)
        for i in range(n):
            if i == 0:
                arr[i] = first
            elif i == 1:
                arr[i] = encoded[i-1] ^ first
            else: 
                arr[i] = encoded[i-1] ^ arr[i-1]
        return arr
