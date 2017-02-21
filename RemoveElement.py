class RemoveElement(object):
    """
    Given an array and a value, remove all instances of that value in place and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Example:
        Given input array nums = [3,2,2,3], val = 3
        Your function should return length = 2, with the first two elements of nums being 2.

    Hint:
        Try two pointers.Show More Hint 
        Subscribe to see which companies asked this question.
    """
    def removeElementMine(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[k] == val:
                del nums[k]
                k -= 1
            if k == len(nums):
                return k
            else:
                k += 1
        return len(nums)

    def removeElementSolution(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start