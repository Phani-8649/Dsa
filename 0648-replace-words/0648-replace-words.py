class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        w=sentence.split()
        for i in range(len(w)):
            for j in range(len(dictionary)):
                if w[i].startswith(dictionary[j]):
                    w[i]=dictionary[j]
        return ' '.join(w)