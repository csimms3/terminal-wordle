import random
import string

words = "words.txt"

def load_words(file):

    print("Loading word list from file...")
    inFile = open(file, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words(words)

class colour:
   green = '\033[1;32;48m'
   yellow = '\033[1;33;48m'
   red = '\033[1;31;48m'
   end = '\033[1;37;0m'

def colour_letter(letter, col):
    return f"{col}{letter}{colour.end}"

def choose_word(word=random.choice(wordlist)):
    return word

def get_frequency_dict(word):
    freq = {}
    for x in word:
        freq[x] = freq.get(x, 0) + 1
    return freq

def generate_alphabet_list():
    lst = []
    for letter in string.ascii_lowercase:
        lst.append(letter)
    return lst

def alphabet_pos(letter):
    return string.ascii_lowercase.index(letter)


def colour_word(guess, word):
    """assumes both guess and word are 5 letters long"""
    result = ""
    letter_dict = get_frequency_dict(word)

    for pos, letter in enumerate(guess):

        if letter in word and letter_dict[letter] > 0:
            if guess[pos] == word[pos]:
                result = result + colour_letter(letter, colour.green)
            else:
                result = result + colour_letter(letter, colour.yellow)

            letter_dict[letter] -= 1
        else:
            result = result + letter
        result = result + " "

    return result

def update_remaining_letters(guess, word, remaining_letters):
    for pos, letter in enumerate(guess):
        letter_pos = alphabet_pos(letter)
        if letter in word:
            if guess[pos] == word[pos]:
                remaining_letters[letter_pos] = colour_letter(letter, colour.green)
            else:
                remaining_letters[letter_pos] = colour_letter(letter, colour.yellow)
        else:
            remaining_letters[letter_pos] = colour_letter(letter, colour.red)
    return remaining_letters

def display_remaining_letters(remaining_letters):
    letter_string = ""
    for pos, val in enumerate(remaining_letters):
        letter_string += f"{val} "
    return letter_string


def wordle():
    remaining_letters = generate_alphabet_list()
    word = choose_word()
    num_guesses = 6
    word_guessed = False

    print("Welcome to Terminal Wordle.")
    print("----------------------------")
    print("You have to guess the five-letter word this program has chosen. You have 6 tries.")
    print(f"{colour.green}Green{colour.end} letters mean: correct letter & position")
    print(f"{colour.yellow}Yellow{colour.end} letters mean: correct letter, wrong position")
    print(f"{colour.red}Red{colour.end} letters mean: already guessed, not in word")
    print("----------------------------")
    print("Good Luck!")
    print("Type your guesses beside the \">>\".")
    print("----------------------------")

    while num_guesses > 0:

        guess = input(">> ").lower()
        if not len(guess) == 5 or guess not in wordlist:
            print("invalid guess")
        else:
            num_guesses -= 1
            remaining_letters = update_remaining_letters(guess, word, remaining_letters)
            print(f"{colour_word(guess, word)}| Letters: {display_remaining_letters(remaining_letters)}| Guesses left: {num_guesses}")

            if guess == word:
                word_guessed = True
                break

    if word_guessed:
        print("Congrats, you guessed it!")
    else:
        print(f"You ran out of guesses, the word was {word}.")


if __name__ == "__main__":
    wordle()

