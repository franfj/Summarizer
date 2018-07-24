from math import log


class TfIdf(object):
    """
    TF-IDF implementation for text summarization.
    """

    @staticmethod
    def get_tf_idf(sentences):
        # Calculate TF
        tf_dictionaries = []
        for sentence in sentences:
            sentence_dict = {}
            for word in sentence:
                sentence_dict[word] = TfIdf.get_term_frequency(word, sentence)
            tf_dictionaries.append(sentence_dict)

        # Calculate IDF
        idf_dict = {}
        for tf_dict in tf_dictionaries:
            for word in tf_dict:
                idf_dict[word] = TfIdf.get_inverse_document_frequency(word, sentences)
        tf_idf_dictionaries = []

        # Calculate TF-IDF
        for tf_dict in tf_dictionaries:
            tf_idf_dict = {}
            # Preload values
            for idf in idf_dict:
                tf_idf_dict[idf] = 0.0

            for tf in tf_dict:
                tf_idf_dict[tf] = tf_dict[tf] * idf_dict[tf]
            tf_idf_dictionaries.append(tf_idf_dict)

        return tf_idf_dictionaries

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
