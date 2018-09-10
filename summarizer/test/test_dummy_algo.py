import unittest

# path imports
import __init__ as path_appends

from summ import Summ
from text_summarizer import summarizer


class DummyAlgoTestCase(unittest.TestCase):
    """ Tests for dummy_algo.py """

    def test_single_sentence_input(self):
        summarizer.text = "This is a sentence."
        summarizer.algo = Summ.DUMMY
        summarizer.percentage = 0.25

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."

        self.assertTrue(expected_result == summarizer.summarize())

    def test_multiple_sentences_input(self):
        summarizer.text = "This is a sentence. \n This is another sentence."
        summarizer.algo = Summ.DUMMY
        summarizer.percentage = 0.25

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."

        self.assertTrue(expected_result == summarizer.summarize())

    def test_empty_input(self):
        summarizer.text = ""
        summarizer.algo = Summ.DUMMY
        summarizer.percentage = 0.25

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."

        self.assertTrue(expected_result == summarizer.summarize())


if __name__ == '__main__':
    unittest.main()
