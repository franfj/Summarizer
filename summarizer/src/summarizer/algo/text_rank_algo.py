from nltk.corpus import stopwords

from abstract_summarizer_algo import AbstractSummarizerAlgo
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

        processed_sentences = []
        for sentence in original_sentences:
            processed_sentences.append(Utils.get_bag_of_words(sentence))

        for i in range(0, len(processed_sentences)):
            for word in processed_sentences[i]:
                if word in stopwords.words(text_lang):
                    processed_sentences[i].remove(word)

        return original_sentences[0]
