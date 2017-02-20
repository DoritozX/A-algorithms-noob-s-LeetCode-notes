class RemoveDuplicates(object):
    """
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    For example,
    Given input array nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

    Subscribe to see which companies asked this question.
    """
    def removeDuplicatesMine(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 9999999
        l = len(nums) - 1
        for i in range(l, -1, -1):
            if nums[i] == j:
                del nums[i + 1]
            else:
                j = nums[i]
        return len(nums)

    def removeDuplicatesSolution(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1