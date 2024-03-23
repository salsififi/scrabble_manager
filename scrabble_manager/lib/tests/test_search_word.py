"""Tests for function search_word in functions.py"""

import sys
from pathlib import Path

FUNCTIONS_FOLDER = Path(__file__).parents[1]
sys.path.append(str(FUNCTIONS_FOLDER))
from functions import search_word
from GLOBALS import WORDS_LIST

def test_with_existing_word():
    assert search_word("POULIES", WORDS_LIST)

def test_with_unexisting_word():
    assert not search_word("ZRTP", WORDS_LIST)

def test_with_letters_contained_in_ohter_words():
    assert not search_word("TRO", WORDS_LIST)

def test_with_lowercase():
    assert search_word("coucou", WORDS_LIST)

if __name__ == '__main__':
    test = search_word("WON", WORDS_LIST)
    print(test)