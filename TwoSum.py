class TwoSum(object):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """
    def twoSumMine(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums.count(target/2) >= 2:
            x = nums.index(target/2)
            nums[x] = "a"
            return [x, nums.index(target/2)]
            
        nums1 = [i for i in nums if i > target / 2]
        nums2 = list(set(nums).difference(set(nums1)))
        for i in nums1:
            for j in nums2:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]

    def twoSumSolution(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i