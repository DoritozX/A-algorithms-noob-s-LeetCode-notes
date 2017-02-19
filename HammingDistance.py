class HammingDistance(object):
    """
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    Given two integers x and y, calculate the Hamming distance.
    Note:
        0 ¡Ü x, y < 231.

    Example:

        Input: x = 1, y = 4
        Output: 2
        Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ¡ü   ¡ü
        The above arrows point to positions where the corresponding bits are different.
    """
    def hammingDistanceMine(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0
        a = max(x,y)
        b = min(x,y)
        
        x = a
        y = b
        
        xBin = bin(x)
        xLen = len(xBin)
        xBin = xBin[2:xLen]
        
        yBin = bin(y)
        yLen = len(yBin)
        yBin = yBin[2:yLen]
        hamDis = 0
        if not len(xBin) == len(yBin):
            for j in range(abs(len(xBin) - len(yBin))):
                yBin = "0" + yBin
        for i in range(len(yBin)):
            if not xBin[i] == yBin[i]:
                hamDis += 1
        return hamDis

    def hammingDistanceSolution(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        