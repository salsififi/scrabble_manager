"""Functions called in main.py"""

def welcome():
    """Displays a welcome screen"""
    print()
    print("-" * 50)
    print(" SCRABBLE MANAGER ".center(50, "*"))
    print("-" * 50)

def validate_user_input(user_input: str) -> bool:
    """True if user_input is a string with only letters (without accents)"""
    return user_input.isalpha() and user_input.isascii()

def ask_letters(quit_key: str) -> str:
    """Asks user which letters were drawn, and return them,
    or leaves program if quit_key is chosen."""
    valid = False
    while not valid:
        print()
        letters = input("Quel est votre tirage ? (Q pour quitter) ").upper()
        valid = validate_user_input(letters)
        if not valid:
            print("Saisie invalide. Inscrivez uniquement des lettres "
                  "sans espaces ni accents.")
    print()
    return letters

def search_scrabbles(letters: str, words: list) -> list:
    """Returns possible scrabbles in a list"""
    return [word for word in words if sorted(letters) == sorted(word)]

def search_word(word: str, words: list) -> bool:
    """True if word exists in words (the dictionary), False otherwise."""
    word = word.upper()
    return word in words

def count_letters_occurrences(word: str) -> dict:
    """Returns a dict object with for keys the letters of word, 
    and for values their numbers of occurrences in word."""
    occurrences = {}
    for letter in word:
        letter = letter.upper()
        occurrences[letter] = occurrences.setdefault(letter, 0) + 1
    return occurrences

def find_possible_words(letters: str, words: list) -> list:
    """Find all 2-letters or more words possible with letters existing
    in dictionary

    Args:
        letters (str): player's letters ()
        words (list): french dictionary

    Returns:
        list: possible words sorted by length (from longest to shortest), 
        then by alphabetical order)
    """
    possible_words = []
    letters = letters.upper()
    for word in words:
        # on élimine les mots d'1 lettre
        if len(word) < 2:
            continue
        # on compte les occurrences des lettres du mot du dictionnaire
        letters_occurrences = count_letters_occurrences(word)
        # chaque lettre doit être contenue dans le tirage, 
        # au moins autant de fois que dans le mot du dico
        for letter in letters_occurrences:
            if letters.count(letter) < letters_occurrences[letter]:
                break
        else:
            possible_words.append(word)    
    possible_words.sort(key=lambda word: (- len(word), word))
    return possible_words


# # Pour les tests
# if __name__ == '__main__':

#     pass