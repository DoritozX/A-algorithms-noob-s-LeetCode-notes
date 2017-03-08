class Generate(object):
    """
    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    """
    def generateMine(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        returnList = [[1]]
        if numRows == 1:
            return [[1]]
        returnList = [[1]]
        n = 2
        while n <= numRows:
            if n == 2:
                returnList.append([1, 1])
            else:
                listTemp = [1] * n
                for i in range(1, n - 1):
                    listTemp[i] = returnList[n - 2][i - 1] + returnList[n - 2][i]
                returnList.append(listTemp)
            n += 1
        return returnList

    def generateSolution(self, numRows):
        """
        explanation: Any row can be constructed using the offset sum of the previous row. 

        Example:
            1 3 3 1 0 
         +  0 1 3 3 1
         =  1 4 6 4 1
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
