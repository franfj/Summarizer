from nltk.corpus import stopwords

from abstractSummarizerAlgo import AbstractSummarizerAlgo
from summarizer.src.summarizer.tools.utils import Utils


class TextRankAlgo(AbstractSummarizerAlgo):
    """
    TextRankAlgo is a text summarization algorithm implementation based on TextRank & LexRank.
    """

    def run(self, text, percentage):
        # Get sentences
        sentences = Utils.getSentences(text)

        # Get lang
        textLang = Utils.detectLang(text)

        # Calculate output length
        outputLength = Utils.getOutputLength(len(sentences), percentage)

        originalSentences = Utils.getSentences(text)

        processedSentences = []
        for sentence in originalSentences:
            processedSentences.append(Utils.getBagOfWords(sentence))

        for i in range(0, len(processedSentences)):
            for word in processedSentences[i]:
                if word in stopwords.words(textLang):
                    processedSentences[i].remove(word)

        return originalSentences[0]
