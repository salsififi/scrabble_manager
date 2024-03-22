"""
SCRABBLE MANAGER
A program that helps you to cheat at French Scrabble
Date: 5/3/2024
Author: Simon Salvaing
"""

from pathlib import Path

DICO = "french_scrabble_dict.txt"  # fichier avec tous les mots français non accentués
FRENCH_DICT_PATH = Path(__file__).parent / DICO
with open(FRENCH_DICT_PATH, 'r', encoding='utf-8') as f:
    WORDS_LIST = [word for word in f.read().splitlines() if word.isascii()]
QUITTER = "Q"

def bienvenue():
    """Displays a welcome screen"""
    print()
    print("-" * 50)
    print(" SCRABBLE MANAGER ".center(50, "*"))
    print("-" * 50)

def ask_letters() -> str:
    """Asks user which 7 letters (or more) are drawn, and return them"""
    valid = False
    while not valid:
        print()
        letters = input("Quel est votre tirage (7 lettres ou +) ? (Q pour quitter) ").upper()
        valid = (len(letters) >= 7 and all(
            [char.isalpha() and char.isascii() for char in letters]
            )) or letters == QUITTER
        if not valid:
            print("Saisie invalide. Inscrivez uniquement vos 7 lettres (ou +) sans espace ni accent.")
    return letters

def search_scrabbles(letters: str) -> list:
    """Returns possible scrabbles in a list"""
    return [word for word in WORDS_LIST if sorted(letters) == sorted(word)]
    
def main():

    end = False

    bienvenue()
    
    while not end:

        user_letters = ask_letters()
        
        if user_letters == QUITTER:
            end = True
            print("À bientôt ! 👍")
            break
        
        scrabbles = search_scrabbles(user_letters)
        if scrabbles:
            print("La liste des scrabbles possibles avec vos 7 lettres est:")
            for scrabble in scrabbles:
                print(scrabble.upper())
        else:
            print("Aucun scrabble n'est possible avec ce tirage.")

main()
