import math

from iso639 import languages
from langdetect import detect
from nltk.tokenize import sent_tokenize, word_tokenize


class Utils(object):
    """
    Utilities class.
    """

    @staticmethod
    def get_sentences(text):
        return sent_tokenize(text)

    @staticmethod
    def get_bag_of_words(sentence):
        return word_tokenize(sentence)

    @staticmethod
    def detect_lang(text):
        return languages.get(alpha2=detect(text)).name.lower()

    @staticmethod
    def get_output_length(n_sentences, percentage):
        length = math.floor(float(n_sentences) * percentage)

        if length < 1:
            return 1

        return length
