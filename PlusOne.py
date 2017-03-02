class PlusOne(object):
    def plusOneMine(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        digits[len(digits) - 1] += 1
        while n >= 0:
            if digits[n] <= 9:
                return digits
            if digits[n] >= 10:
                digits[n] = 0
                if n == 0:
                    digits.insert(0, 1)
                else:
                    digits[n - 1] += 1
            n -= 1
        return digits