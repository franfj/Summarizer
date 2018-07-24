from algo import DummySummarizerAlgo
from algo import Summ
from algo import TextRankAlgo
from algo import Utils


class Summarizer(object):
    """
    Summarizer is the class used for storing the text to be summarized, 
    the algorithm to use, and the percentage of text desired. 
    Also, is the responsible of calling the run method of the summarization algorithm.
    """

    def __init__(self, text="Dummy Text", algo=Summ.TEXT_RANK, percentage=0.25):
        self._text = text
        self._algo = algo
        self._percentage = percentage

    def summarize(self, text=None, algo=None, percentage=None):
        if text != None:
            self.init_text(text)

        if algo != None:
            self._algo = algo

        if percentage != None:
            self._percentage = percentage

        text_summarizer = SummarizerFactory.factory(self._algo)
        return text_summarizer.run(self._text, self._percentage)

    def schematize(self, text=None, algo=None, percentage=None):
        if text != None:
            self.init_text(text)

        if algo != None:
            self._algo = algo

        if percentage != None:
            self._percentage = percentage

        sentences = Utils.get_sentences(self.summarize())
        output = ''

        for sentence in sentences:
            output += '- ' + sentence + '\n'
        return output

    def init_text(self, text):
        try:
            text = text.encode('utf-8')
        except:
            pass

        # Add final point if it does not exist
        text = text.strip()
        if text[-1:] is not '.':
            text += '.'

        # Remove line feeds
        new_text = ''

        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line and line[-1:] is not '.':
                line += '.'
            new_text += " " + line

        self._text = new_text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if type(value) == str:  # type checking
            self.init_text(value)
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
The text_summarizer instance to be imported.
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

        if algo.lower() == Summ.TEXT_RANK.lower():
            return TextRankAlgo()
