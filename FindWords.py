class FindWords(object):
    def findWordsMine(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        line2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        line3 = ["z", "x", "c", "v", "b", "n", "m"]
        keyBoard = [line1, line2, line3]
        outPut = words[:]
        for wordOriginal in words:
            word = wordOriginal.lower()
            for line in keyBoard:
                if word[0] in line:
                    for i in range(1, len(word)):
                        if not word[i] in line:
                            outPut.remove(wordOriginal)
                            break
        return outPut
        