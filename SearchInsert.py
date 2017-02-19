class SearchInsert(object):
    """
    Total Accepted: 147713
    Total Submissions: 377528
    Difficulty: Easy
    Contributors: Admin
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Here are few examples.
    [1,3,5,6], 5 ¡ú 2
    [1,3,5,6], 2 ¡ú 1
    [1,3,5,6], 7 ¡ú 4
    [1,3,5,6], 0 ¡ú 0

    Subscribe to see which companies asked this question.
    """
    def searchInsertMine(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        last = 0
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    last = i
            if (last == 0) and (nums[0] > target):
                return(last)
            else:
                return(last + 1)

    def searchInsertSolution(self, nums, key):
        if key > nums[len(nums) - 1]:
            return len(nums)

        if key < nums[0]:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)/2
            if nums[m] > key:
                r = m - 1
                if r >= 0:
                    if nums[r] < key:
                        return r + 1
                else:
                    return 0

            elif nums[m] < key:
                l = m + 1
                if l < len(nums):
                    if nums[l] > key:
                        return l
                else:
                    return len(nums)
            else:
                return m
