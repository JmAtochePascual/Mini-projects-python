# Guess the number
import random

random_number = random.randint(1, 100)
oportunity = 8
attempts = 0

nombre = input("Enter your name: ")
print(f"""
==== GUESS THE NUMBER ====

Hello {nombre},
You have {oportunity} opportunities to guess the number

==== GUESS THE NUMBER ====
""")

for i in range(oportunity):
    numero = int(input("Enter a number between 1 and 100: "))
    attempts += 1
    if numero < 1 or numero > 100:
        print("\nInvalid input, please enter a number between 1 and 100")
    elif numero == random_number:
        print(f"\nCongratulations {nombre}, you guessed the number! in {attempts} attempts")
        exit()
    elif numero < random_number:
        print("\nToo low, try again")
    else:
        print("\nToo high, try again")

print(f"\n:c {nombre}, you lost the game")