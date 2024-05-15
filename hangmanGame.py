# Your Code
import random

logo = '''

 +-+-+-+-+ +-+-+-+-+-+-+-+
 |F|k|'|s| |H|a|n|g|m|a|n|
 +-+-+-+-+ +-+-+-+-+-+-+-+

'''

stages = [
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """

]

word_list = ["physics", "chemistry", "maths", "biology",]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

print(logo)

display = []
for _ in chosen_word:
  display.append("_")

print(stages[lives])
print(*display, "\n")


while True:

  while True:
    guess = input("Guess a Letter: ").lower()
    if len(guess) == 1:
      break
    print("Please Enter a Single Character to Continue: \n")

  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      print("Your Guess is Correct! ")
      display[position] = chosen_word[position]

  if "_" not in display:
    print("Good!, You WON the Game!!!!")
    break

  if guess not in chosen_word:
    print("Your Guess is Wrong XXX")
    lives -= 1
    print(stages[lives])
    print(f"You left with {lives} lives")

  if lives == 0:
    print("YOU LOSE!!!!!!!! Games is OVER! ")
    break

  print(*display)

print(f"The Answer: {chosen_word}")