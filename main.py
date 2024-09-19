import random
from hangman_words import word_list
from hangman_art import stages, logo

#print the hangman logo from hangman_art
print(logo)

#randomly chose a word from the word_list
chosen_word = random.choice(word_list)

print("\nYour word to guess: ", end="")

for letter in chosen_word:
    print("_", end="")


guessed_letters = []    # create a list to hold the guessed letters
game_over = False       # create a varialble to end the game
lives = 6               # variable to keep track of the number of lives left

while not game_over:
    print(f"\n\n****************************{lives}/6 LIVES LEFT****************************")

    # user input
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"\nYou've already guessed {guess}. Try again" )

    #display reveals the letter in the correct position and _ in the rest of the positions
    display = ""

    #check if the letter guessed in the chosen word
    for letter in chosen_word:
        if letter == guess:
            display += guess
            guessed_letters.append(guess)
            
        #elif statement to add previous guesses to display
        elif letter in guessed_letters:     
            display += letter
        else:
            display += "_"
        
    print("\nWord to guess:" + display)

    #if the letter guess is not in the word lose one life
    if guess not in chosen_word and guess not in guessed_letters:
        print(f"\nYou guess {guess}, that's not in the word. You lose a life")
        lives -= 1

    #lose the game when lives equal to 0
        if lives == 0:
            game_over = True   
            print(f"\n***********************IT WAS {chosen_word}! YOU LOSE**********************")

    guessed_letters.append(guess)

    #when the display has no more blanks user wins
    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************")
    
    #print the ASCII art from hangman_art
    print(stages[lives])