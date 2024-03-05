"""
SCRABBLE MANAGER
A program to help you to find best words at French Scrabble
Date: 5/3/2024
Author: Simon Salvaing
"""

import os
DICO = "french_dict_raw.txt"  # fichier avec tous les mots français non accentués
FRENCH_DICT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DICO)

with open(FRENCH_DICT_PATH, 'r', encoding='utf-8') as f:
    WORDS_LIST = [word for word in f.read().splitlines() if word.isascii()]

def bienvenue():
    """Displays a welcome screen"""
    print()
    print("-" * 50)
    print(" SCRABBLE MANAGER ".center(50, "*"))
    print("-" * 50)

def ask_letters() -> str:
    """Asks user which 7 letters are drawn, and return them"""
    valid = False
    while not valid:
        print()
        letters = input("Quelles sont vos 7 lettres ? ").lower()
        valid = len(letters) == 7 and all(
            [char.isalpha() and char.isascii() for char in letters]
            )
        if not valid:
            print("Saisie invalide. Inscrivez uniquement vos 7 lettres sans espace ni accent.")
    return letters

def search_scrabbles(letters: str) -> list:
    """Returns possible scrabbles in a list"""
    return [word for word in WORDS_LIST if sorted(letters) == sorted(word)]
    
def main():

    end = False

    bienvenue()
    
    while not end:
        user_letters = ask_letters()

        scrabbles = search_scrabbles(user_letters)
        if scrabbles:
            print("La liste des scrabbles possibles avec vos 7 lettres est:")
            for scrabble in scrabbles:
                print(scrabble.upper())
        else:
            print("Aucun scrabble n'est possible avec ce tirage.")
        
        print()
        user_choice = input("Voulez-vous continuer avec un autre tirage ? (O pour Oui) ").upper()
        if user_choice != "O":
            print("À bientôt ! 👍")
            end = True

main()
