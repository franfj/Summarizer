from math import sqrt


class CosineSimilarity(object):
    """
    Cosine similarity implementation for text summarization.
    """

    @staticmethod
    def get_cosine_similarity(tf_idf_a, tf_idf_b):
        dot_product = CosineSimilarity.get_dot_product(tf_idf_a, tf_idf_b)
        magnitude_a = CosineSimilarity.get_magnitude(tf_idf_a)
        magnitude_b = CosineSimilarity.get_magnitude(tf_idf_b)

        return dot_product / (magnitude_a * magnitude_b)

    @staticmethod
    def get_magnitude(tf_idf):
        magnitude = 0.0

        for word in tf_idf:
            magnitude += pow(tf_idf[word], 2)

        return sqrt(magnitude)

    @staticmethod
    def get_dot_product(tf_idf_a, tf_idf_b):
        dot_product = 0.0

        for word in tf_idf_a:
            dot_product += tf_idf_a[word] * tf_idf_b[word]

        return dot_product
