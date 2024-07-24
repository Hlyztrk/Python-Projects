import os
import random
import time
from hangman_art import HANGMANART, HANGMAN

# Create a list of words from txt file
def create_words_list(text_file):
    word_list = []
    with open(text_file, 'r') as w_list:
        word_list = [i.replace("\n","") for i in w_list]
    return word_list

# Check if a letter has already been used
def check_used_letter(used_letter_list, guessed_letter):
    guessed_letter_count = used_letter_list.count(guessed_letter)
    if guessed_letter_count > 1:
        print(f"You have already used letter \"{guessed_letter}\". Try another one.")


# Find if the guessed letter exists in the random word
def hangman(random_word, guessed_word, hidden_word):
    for i in range(len(random_word)):
        letter = random_word[i]
        if guessed_word == letter:
            hidden_word[i] = guessed_letter
    return hidden_word

# Clear screen after every guess
def clear_screen():
    time.sleep(1)
    os.system("clear")

word_list = create_words_list("words_list.txt")

random_word = random.choice(word_list)
secret_word = [ x.replace(x,'_') for x in random_word]

wrong_guess_count = 0
used_letters_list =[]
while wrong_guess_count <= len(HANGMANART) -1:
    print(HANGMAN)
    print(HANGMANART[wrong_guess_count])
    if "_" not in secret_word:
        print(" ".join(secret_word))
        print("Well done! You saved your neck ;)")
        break
    print(" ".join(secret_word))
    guessed_letter = input("Guess a letter: ")
    used_letters_list += guessed_letter
    check_used_letter(used_letters_list, guessed_letter)
    hangman(random_word, guessed_letter, secret_word)
    if guessed_letter not in random_word: 
        wrong_guess_count += 1
    if wrong_guess_count == len(HANGMANART) - 1:
        clear_screen()
        print(HANGMANART[wrong_guess_count])
        print("You are out of lives :(")
        print(f"The word was: {random_word}")
        break
    clear_screen()







