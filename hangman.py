import random
from traceback import print_tb
from hangman_art import stages
from replit import clear


with open ("turkce_kelime_listesi.txt","r", encoding = "utf-8") as dosya:
    liste =[satir.strip() for satir in dosya.readlines()]


chosen_word=  random.choice(liste)
kelime = chosen_word
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess the letter : ").lower()
    clear()

    if guess in display:
        print(f"You have already guessed in {guess}")


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)


    if guess not in chosen_word:
        print(f"Your guessed the {guess}, that is not in word.Your losing life.")
        lives -= 1
        if lives == 0 :
            end_of_game = True
            print(kelime)
            print("Game Over")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You Won")


        print(stages[lives])

