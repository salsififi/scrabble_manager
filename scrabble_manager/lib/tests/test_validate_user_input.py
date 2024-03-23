"""Tests for function validate_user_input in functions.py"""

import sys
from pathlib import Path

FUNCTIONS_FOLDER = Path(__file__).parents[1]
sys.path.append(str(FUNCTIONS_FOLDER))
from functions import validate_user_input
from GLOBALS import QUITTER

def test_with_lowercase():
    assert validate_user_input("azerty")

def test_with_3_letters():
    assert validate_user_input("BOA")

def test_with_8_letters():
    assert validate_user_input("PoLoChOn")

def test_with_quit_key():
    assert validate_user_input(QUITTER)

def test_with_string_containing_numbers():
    assert not validate_user_input("AZERTY2")

def test_with_string_containing_accents():
    assert not validate_user_input("école")

def test_with_string_containing_spaces():
    assert not validate_user_input("C O U C O U")

