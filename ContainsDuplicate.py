class ContainsDuplicate(object):
    """
    Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
    """
    def containsDuplicateMine(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(nums):
            if v in dic:
                return True
            dic[v] = i
        return False

    def containsDuplicateSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))