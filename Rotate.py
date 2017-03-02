class Rotate(object):
    """
    Rotate an array of n elements to the right by k steps.

    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

    Note:
        Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

    Hint:
        Could you do it in-place with O(1) extra space?
    """
    def rotateMine(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums
        if len(nums) <= 1:
            return
        kCount = 0
        while kCount < k:
            nums.insert(0, nums[-1])
            del nums[-1]
            kCount += 1

    class RolutionSolution(object):
        def rotateSolution(self, nums, k):
            if k is None or k <= 0:
                return
            k, end = k % len(nums), len(nums) - 1
            self.reverse(nums, 0, end - k)
            self.reverse(nums, end - k + 1, end)
            self.reverse(nums, 0, end)
        
        def reverse(self, nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1