import wordChecker
import unittest

class TestWordChecker(unittest.TestCase):

    def test_rhyme(self):
        wc = wordChecker.WordChecker()
        self.assertTrue(wc.isRhyme("ball", "hall"))

    def test_rhyme(self):
        wc = wordChecker.WordChecker()
        self.assertFalse(wc.isRhyme("crazy", "hall"))

if __name__ == '__main__':
    unittest.main()

