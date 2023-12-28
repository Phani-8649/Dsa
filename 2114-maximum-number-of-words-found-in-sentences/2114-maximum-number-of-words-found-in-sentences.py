class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_word_count = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            max_word_count = max(max_word_count, word_count)
        return max_word_count