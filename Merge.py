class Merge(object):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    Note:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
    """
    def mergeMine(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[0:m]
        nums2[:] = nums2[0:n]
        k = 0
        j = 0
        for i in range(m + n):
            if k == len(nums1):
                nums1[k + 1 : m + n] = nums2[j : n]
                return
            if j == n:
                return
            if nums1[k] < nums2[j]:
                k += 1
            elif nums1[k] > nums2[j]:
                nums1.insert(k, nums2[j])
                j += 1
                k += 1
            elif nums1[k] == nums2[j]:
                nums1.insert(k, nums2[j])
                k += 1
                j += 1

    def mergeSolution(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]