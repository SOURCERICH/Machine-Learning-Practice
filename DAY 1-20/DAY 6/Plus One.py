class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        digits[n - 1] += 1
        carry = 0
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry:
            digits.insert(0, carry)
        
        return digits

