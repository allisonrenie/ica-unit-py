import palindrome
import unittest
import pytest

#pytest
def test_regularize():
    assert palindrome.regularize("hello there") == "hellothere"

def test_regularize2():
    assert palindrome.regularize("HI THERE") == "hithere"

def test_regularize3():
    assert palindrome.regularize("bulbasaur is the best pokemon") == "bulbasauristhebestpokemon"

def test_match():
    assert palindrome.match("meow", "meow")

def test_is_palindrome():
    assert palindrome.is_palindrome("Do GEEse SEE God")

#unittest
#python -m unittest test_palindrome.py
class test_class(unittest.TestCase):
    def test_regularize4(self):
        self.assertEqual(palindrome.regularize('   cats ARE CooL   '), 'catsarecool')

    def test_match(self):
        self.assertTrue(palindrome.match("racecar", "racecar"))

    def test_is_palindrome2(self):
        self.assertTrue(palindrome.is_palindrome("   Red Rum sir is murder   "))
