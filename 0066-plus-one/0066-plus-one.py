class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            num = digits[i] + carry
            if num >= 10:
                digits[i] = num % 10
                carry = 1
            else:
                digits[i] = num
                carry = 0
                break
                
        if carry == 1:
            new = [carry]
            new.extend(digits)
            return new
        return digits