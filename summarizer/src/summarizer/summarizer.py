from algo.dummyAlgo import DummySummarizerAlgo
from algo.summ import Summ


class Summarizer(object):
    """
    Summarizer is the class used for storing the text to be summarized, 
    the algorithm to use, and the percentage of text desired. 
    Also, is the responsible of calling the run method of the summarization algorithm.
    """

    def __init__(self, text="Dummy Text", algo=Summ.DUMMY, percentage=0.25):
        self._text = text
        self._algo = algo
        self._percentage = percentage

    def summarize(self):
        textSummarizer = SummarizerFactory.factory(self._algo)
        return textSummarizer.run(self._text, self._percentage)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if type(value) == str:  # type checking
            self._text = value
        else:
            raise Exception("Invalid value for text")

    @property
    def algo(self):
        return self._algo

    @algo.setter
    def algo(self, value):
        if type(value) == str:  # type checking
            self._algo = value
        else:
            raise Exception("Invalid value for algo")

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if type(value) == float:  # type checking
            self._percentage = value
        else:
            raise Exception("Invalid value for percentage")


"""
The summarizer instance to be imported.
"""
summarizer = Summarizer()


class SummarizerFactory(object):
    """
    SummarizerFactory returns the text summarization algorithm implementation selected.
    """

    @staticmethod
    def factory(algo):
        if algo.lower() == Summ.DUMMY.lower():
            return DummySummarizerAlgo()
