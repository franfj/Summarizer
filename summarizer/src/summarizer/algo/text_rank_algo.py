from abstract_summarizer_algo import AbstractSummarizerAlgo
from summarizer.src.summarizer.tools.tf_idf import TfIdf
from summarizer.src.summarizer.tools.utils import Utils


class TextRankAlgo(AbstractSummarizerAlgo):
    """
    TextRankAlgo is a text summarization algorithm implementation based on TextRank & LexRank.
    """

    def run(self, text, percentage):
        # Get sentences
        sentences = Utils.get_sentences(text)

        # Get lang
        text_lang = Utils.detect_lang(text)

        # Calculate output length
        output_length = Utils.get_output_length(len(sentences), percentage)

        original_sentences = Utils.get_sentences(text)
        processed_sentences = self.initilize_processed_sentences(original_sentences, text_lang)

        tf_dictionaries = []
        for sentence in processed_sentences:
            sentence_dict = {}
            for word in sentence:
                sentence_dict[word] = TfIdf.get_term_frequency(word, sentence)
            tf_dictionaries.append(sentence_dict)

        idf_dict = {}
        for tf_dict in tf_dictionaries:
            for word in tf_dict:
                idf_dict[word] = TfIdf.get_inverse_document_frequency(word, processed_sentences)

        tf_idf_dictionaries = []
        for tf_dict in tf_dictionaries:
            tf_idf_dict = {}
            for tf in tf_dict:
                tf_idf_dict[tf] = tf_dict[tf] * idf_dict[tf]
            tf_idf_dictionaries.append(tf_idf_dict)

        print tf_idf_dictionaries

        return original_sentences[0]

    def initilize_processed_sentences(self, original_sentences, text_lang):
        sentences = []
        for sentence in original_sentences:
            bag_of_words = Utils.get_bag_of_words(sentence.lower())
            bag_of_words = list(set(bag_of_words))  # Remove repeated words
            sentences.append(bag_of_words)

        Utils.remove_stop_words(sentences, text_lang)

        return sentences
