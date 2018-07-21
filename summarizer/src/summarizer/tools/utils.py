import math

from iso639 import languages
from langdetect import detect
from nltk.tokenize import sent_tokenize, word_tokenize


class Utils(object):
    """
    Utilities class.
    """

    @staticmethod
    def getSentences(text):
        return sent_tokenize(text)

    @staticmethod
    def getBagOfWords(sentence):
        return word_tokenize(sentence)

    @staticmethod
    def detectLang(text):
        return languages.get(alpha2=detect(text)).name.lower()

    @staticmethod
    def getOutputLength(nSentences, percentage):
        length = math.floor(float(nSentences) * percentage)

        if length < 1:
            return 1

        return length
