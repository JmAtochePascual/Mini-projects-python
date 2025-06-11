import random
import re
from data.words import words
from data.images import images

# choose a random word
def choose_word() -> str:
  return random.choice(words)

# show the word hidden
def show_word_hidden(word: str) -> str:
  word_hidden = ""
  len_word = len(word)
  for i in range(len_word):
    word_hidden += "_ "
  return word_hidden

# ask for a letter
def ask_letter() -> str:
  return input("Enter a letter: ").lower()

# validate the letter
def validate_letter(letter: str) -> bool:
  pattern = r'^[a-zA-Z]+$'
  if not re.match(pattern, letter):
    print("\nPlease enter a letter")
    return False
  
  if len(letter) > 1:
    print("\nPlease enter only one letter")
    return False
  
  return True

# check if the letter is in the word
def check_letter(word: str, letter: str) -> bool:
  return letter in word

# check the position of the letter
def check_position(word: str, letter: str) -> list:
  position_letter = []
  for i in range(len(word)):
    if word[i] == letter:
      position_letter.append(i)
  return position_letter

# if the letter is in the word, show the letter
def show_letter(word_hidden: str, letter: str, position_letter: list) -> str:
  word_hidden_list = word_hidden.split(" ")
  
  for i in position_letter:
    word_hidden_list[i] = letter
  return " ".join(word_hidden_list)

# if the letter is not in the word, reduce the attempts
def reduce_attempts(attempts: int) -> int:
  return attempts - 1

print("""
==== AHORCADO ====

Enter a letter to guess the word

==== AHORCADO ====
\n""")


def init():
  word = choose_word()
  word_hidden = show_word_hidden(word)
  attempts = 6
  letter = ""
  letter_valid = False
  counter = 0
  
  print(images[0])
  
  print(f"{word_hidden}\n")
  print(f"\nAttempts: {attempts}")
  
  while attempts > 0:
    
    while not letter_valid:
      letter = ask_letter()
      letter_valid = validate_letter(letter)
      
    if check_letter(word, letter):
      position_letter = check_position(word, letter)
      word_hidden = show_letter(word_hidden, letter, position_letter)
      print(images[counter])
      print(f"{word_hidden}\n") 
      print(f"\nAttempts: {attempts}")
      
      if word_hidden.replace(" ", "") == word:
        print(f"\nCongratulations, you guessed the word {word}")
        exit()
      else:
        letter_valid = False
    else:
      attempts = reduce_attempts(attempts)
      letter_valid = False
      counter += 1
      print(images[counter])
      print(f"{word_hidden}\n") 
      print(f"\nAttempts: {attempts}")
  
  print(f"""
  ======== THANKS FOR PLAYING ========
  :c, you lost the game
  The word was: {word}
  ======== THANKS FOR PLAYING ========
  """)

init()
