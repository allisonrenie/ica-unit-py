import unittest
import pytest
import word_count

#pytest
def test_count_words():
    assert word_count.count_words('do you like pancakes?') == 4

def test_word_count2():
    assert word_count.count_words('         do you like pancakes?        ') == 4
    assert word_count.count_words('                 hi             ') == 1

#unittest
#python -m unittest test_word_count.py
class test_class(unittest.TestCase):
    def test_count_words3(self):
        self.assertEqual(word_count.count_words('ikea shark'), 2)
        
    def test_count_words4(self):
        self.assertEqual(word_count.count_words('   paradise lost by john milton     '), 5)
