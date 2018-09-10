import unittest

# path imports
import __init__ as path_appends

from algo import DummySummarizerAlgo


class DummyAlgoTestCase(unittest.TestCase):
    """ Tests for dummy_algo.py """

    def test_single_sentence_input(self):
        text = "This is a sentence."
        percentage = 0.25

        dummy_summarizer = DummySummarizerAlgo()

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."
        self.assertTrue(expected_result == dummy_summarizer.run(text, percentage))

    def test_multiple_sentences_input(self):
        text = "This is a sentence. \n This is another sentence."
        percentage = 0.25

        dummy_summarizer = DummySummarizerAlgo()

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."
        self.assertTrue(expected_result == dummy_summarizer.run(text, percentage))

    def test_empty_input(self):
        text = ""
        percentage = 0.25

        dummy_summarizer = DummySummarizerAlgo()

        expected_result = "DUMMY TEXT. DUMMY TEXT. DUMMY TEXT."
        self.assertTrue(expected_result == dummy_summarizer.run(text, percentage))


if __name__ == '__main__':
    unittest.main()
