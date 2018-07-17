from algo.dummyAlgo import DummySummarizerAlgo
from algo.summ import Summ


class Summarizer(object):
    def __init__(self, text="Dummy Text", algo=Summ.DUMMY, percentage=0.0):
        self._text = text
        self._algo = algo
        self._percentage = percentage

    def run(self):
        textSummarizer = SummarizerFactory.factory(self._algo)
        return textSummarizer.run(self._text, self._percentage)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def algo(self):
        return self._algo

    @algo.setter
    def algo(self, value):
        self._algo = value

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value


summarizer = Summarizer()


class SummarizerFactory(object):
    @staticmethod
    def factory(algo):
        if algo == Summ.DUMMY:
            return DummySummarizerAlgo()
