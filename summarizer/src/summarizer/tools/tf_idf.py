from math import log


class TfIdf(object):
    """
    TF-IDF class.
    """

    @staticmethod
    def get_term_frequency(word, sentence):
        return sentence.count(word.lower()) / float(len(sentence))

    @staticmethod
    def get_inverse_document_frequency(word, sentences):
        occurrences = 0
        for sentence in sentences:
            if word in sentence:
                occurrences += 1

        if occurrences > 0:
            return 1.0 + log(float(len(sentences)) / occurrences)
        else:
            return 1.0
