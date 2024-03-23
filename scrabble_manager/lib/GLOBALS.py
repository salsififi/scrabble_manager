"""Global constants"""

from pathlib import Path

# dictionary (.txt file) with all french accent-stripped words
DICO = "french_scrabble_dict.txt"

# dictionary path
FRENCH_DICO_PATH = Path(__file__).parent.parent / DICO

# words list
with open(FRENCH_DICO_PATH, 'r', encoding='utf-8') as f:
    WORDS_LIST = [word for word in f.read().splitlines() if word.isascii()]

# keys for menu
QUITTER = "Q"
