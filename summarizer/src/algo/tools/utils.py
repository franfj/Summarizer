import math

from iso639 import languages
from langdetect import detect
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


class Utils(object):
    """
    Utilities class.
    """

    @staticmethod
    def get_sentences(text):
        sentences = []
        for sentence in sent_tokenize(text):
            sentences.append(sentence[:-1])  # Remove punctuation

        return sentences

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

        return int(length)

    @staticmethod
    def remove_stop_words(sentences, text_lang):
        for i in range(0, len(sentences)):
            for word in sentences[i]:
                try:
                    if word in stopwords.words(text_lang):
                        sentences[i].remove(word)
                except IOError:
                    return
