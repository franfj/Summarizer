from nltk.tokenize import word_tokenize


class Utils(object):
    """
    Utilities class.
    """

    @staticmethod
    def getSentences(text):
        return sent_tokenize(text)
