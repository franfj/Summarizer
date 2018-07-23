from abstract_summarizer_algo import AbstractSummarizerAlgo
from tools import TfIdf, Utils, CosineSimilarity


class TextRankAlgo(AbstractSummarizerAlgo):
    """
    TextRankAlgo is a text summarization algorithm implementation based on TextRank & LexRank.
    """

    def run(self, text, percentage):
        # Avoid decoding errors
        text = text.decode('utf-8')

        # Get sentences
        sentences = Utils.get_sentences(text)

        # Get lang
        text_lang = Utils.detect_lang(text)

        # Calculate output length
        output_length = Utils.get_output_length(len(sentences), percentage)

        original_sentences = Utils.get_sentences(text)
        processed_sentences = self.initilize_processed_sentences(original_sentences, text_lang)

        tf_idf_dictionaries = TfIdf.get_tf_idf(processed_sentences)

        cosine_similarities = {}
        for i in range(0, len(tf_idf_dictionaries)):
            aux = 0.0
            for j in range(0, len(tf_idf_dictionaries)):
                if i != j:
                    aux += CosineSimilarity.get_cosine_similarity(tf_idf_dictionaries[i], tf_idf_dictionaries[j])
            cosine_similarities[i] = aux

        sorted_sentences = sorted(cosine_similarities, key=cosine_similarities.get, reverse=True)

        output_sentences = []
        for i in range(0, output_length):
            output_sentences.append(sorted_sentences[i])

        output_sentences = sorted(output_sentences)

        output = ''
        for i in output_sentences:
            output += original_sentences[i] + '. '

        return output

    def initilize_processed_sentences(self, original_sentences, text_lang):
        sentences = []
        for sentence in original_sentences:
            bag_of_words = Utils.get_bag_of_words(sentence.lower())
            bag_of_words = list(set(bag_of_words))  # Remove repeated words
            sentences.append(bag_of_words)

        Utils.remove_stop_words(sentences, text_lang)

        return sentences
