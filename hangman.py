from words import words
import random
import string

def get_word(words):
    chosen_word = random.choice(words)
    while '-' in chosen_word or ' ' in chosen_word:
        chosen_word = random.choice(words)
    return chosen_word.upper()

def hangman():
    chosen_word = get_word(words)
    chosen_word_letters = set(chosen_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(chosen_word_letters) > 0:
        print('You have used these letters: ', ''.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in chosen_word]
        print(f'Current word: ', ''.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in chosen_word_letters:
                chosen_word_letters.remove(user_letter)

        elif user_letter in used_letters:
            return 'Already used!'
    
        else:
            return 'Invalid char'


hangman()