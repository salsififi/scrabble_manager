"""Tests for function find_possible_words in functions.py"""

import sys
from pathlib import Path

FUNCTIONS_FOLDER = Path(__file__).parents[1]
sys.path.append(str(FUNCTIONS_FOLDER))
from functions import find_possible_words
from GLOBALS import WORDS_LIST

def test_with_PPPAAAR():
    assert find_possible_words("PPPAAAR", WORDS_LIST) == [
        'PAPA', 'PARA', 'RAPA', 'ARA', 'PAR', 'RA'
        ]
    
def test_with_CoUcOuS():
    assert find_possible_words("CoUcOuS", WORDS_LIST) == [
        'COUCOUS', 'COUCOU', 'COCOS', 'COCUS', 'COUSU', 'COCO', 
        'COCU', 'COUS', 'COU', 'SOC', 'SOU', 'SUC', 'CC', 'OC', 
        'OS', 'OU', 'SU', 'US'
        ]
    

if __name__ == "__main__":
    test = find_possible_words("TROUDUC", WORDS_LIST)
    print(test)