class FindWords(object):
    """
    Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

    Example 1:
        Input: ["Hello", "Alaska", "Dad", "Peace"]
        Output: ["Alaska", "Dad"]
    Note:
        You may use one character in the keyboard more than once.
        You may assume the input string will only contain letters of alphabet.
        Subscribe to see which companies asked this question.
    """
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
        
    def findWordsSolution(self, words):
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)