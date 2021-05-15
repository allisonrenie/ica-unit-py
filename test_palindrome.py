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
    
#unittest
