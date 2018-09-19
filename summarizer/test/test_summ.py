import unittest

# path imports
import __init__ as path_appends

from algo import Summ


class SummTestCase(unittest.TestCase):
    """ Tests for summ.py """

    def test_dummy_enum(self):
        self.assertTrue(Summ.DUMMY == "dummy")

    def test_text_rank_enum(self):
        self.assertTrue(Summ.TEXT_RANK == "textRank")


if __name__ == '__main__':
    unittest.main()
