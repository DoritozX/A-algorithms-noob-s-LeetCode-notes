class MissingNumber(object):
    """
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
    For example,
    Given nums = [0, 1, 3] return 2.
    Note:
        Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
    Credits:
        Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
        Subscribe to see which companies asked this question.
    """
    def missingNumberMine(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set(list(range(len(nums) + 1))) - set(nums))[0]

    def missingNumber(self, nums):
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]