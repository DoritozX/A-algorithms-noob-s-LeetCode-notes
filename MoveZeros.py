class MoveZeros(object):
    """
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

    Note:
        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.
    Credits:
        Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

        Subscribe to see which companies asked this question.
    """
    def moveZeroesMine(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

    def moveZerosSolution(self, nums):

        nums.sort(key= lambda x: 1 if x == 0 else 0)