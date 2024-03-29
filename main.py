"""
SCRABBLE MANAGER
A program that helps you to cheat at French Scrabble
Date of 1st version: 5/3/2024
Author: Simon Salvaing
"""

import typer

from scrabble_manager.lib.GLOBALS import QUITTER, WORDS_LIST, SCRABBLE
from scrabble_manager.lib.functions import (
    welcome, ask_letters, search_scrabbles, find_possible_words, search_word
    )

def main():

    end = False
    
    welcome()
    while not end:

        user_letters = ask_letters(quit_key=QUITTER)
        if user_letters == QUITTER:
            end = True
            print("À bientôt ! 👍")
            break
        
        possible_words = find_possible_words(user_letters, WORDS_LIST)
        if possible_words:
            print("Voici la liste de tous les mots possibles:")
            for i, word in enumerate(possible_words):
                if len(word) >= 7:
                    print(typer.style(f"{word.upper()}",
                                      fg=typer.colors.WHITE, 
                                      bg=typer.colors.BLUE), SCRABBLE)
                else:
                    print(f"{word.capitalize()}", end=" - " 
                          if i < len(possible_words) - 1 else "\n")      
        else:
            print("Votre tirage est vraiment trop pourri ! 😭")

if __name__ == '__main__':
    main()
