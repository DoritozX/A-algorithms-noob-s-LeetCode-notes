class TwoSumII(object):
    """
    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution and you may not use the same element twice.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2
    """
    def twoSumIIMine(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,v in enumerate(numbers, start = 1):
            if v in dic:
                if v == target / 2:
                    return [i - 1, i]
                else:
                    dic[v] = i
            else:
                dic[v] = i
            if target - v in dic and dic[target - v] != dic[v]:
                return [dic[target - v], dic[v]]

    # two-pointer
    def twoSumIISolutionTwoPointer(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
 
    # dictionary           
    def twoSumIISolutionDictionary(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
 
    # binary search        
    def twoSumIISolutionBinarySearch(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1