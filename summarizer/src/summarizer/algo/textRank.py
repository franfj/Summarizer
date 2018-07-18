import math

from abstractSummarizerAlgo import AbstractSummarizerAlgo
from summarizer.src.summarizer.tools.utils import Utils


class TextRankAlgo(AbstractSummarizerAlgo):
    """
    TextRankAlgo is a text summarization algorithm implementation based on TextRank & LexRank.
    """

    def run(self, text, percentage):
        # Get sentences
        sentences = Utils.getSentences(text)
        nSentences = len(sentences)

        # Calculate output length
        nSentencesDesired = math.floor(float(nSentences) * percentage)
        if nSentencesDesired < 1:
            nSentencesDesired = 1
