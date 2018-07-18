from nltk.tokenize import sent_tokenize


class Utils(object):
    """
    Utilities class.
    """

    @staticmethod
    def getSentences(text):
        return sent_tokenize(text)
