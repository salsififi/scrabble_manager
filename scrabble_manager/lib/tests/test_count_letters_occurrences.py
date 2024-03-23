"""Tests for function count_letters_occurrences in functions.py"""

import sys
from pathlib import Path

FUNCTIONS_FOLDER = Path(__file__).parents[1]
sys.path.append(str(FUNCTIONS_FOLDER))
from functions import count_letters_occurrences

def test_with_BALAI():
    assert count_letters_occurrences("BALAI") == {
        "B": 1, "A": 2, "L": 1, "I": 1
        }

def test_with_ExceLlenCE():
    assert count_letters_occurrences("ExceLlenCE") == {
        "E": 4, "X": 1, "C": 2, "L": 2, "N": 1
        }
    