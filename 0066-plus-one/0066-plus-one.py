class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i > -1 and carry:
            curr = digits[i]
            digits[i] = (curr + carry) % 10
            carry = (curr + carry) // 10
            if i == 0 and carry:
                return [1] + digits
            i -= 1
        return digits