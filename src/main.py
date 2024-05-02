import random
# gets the word list
from words import word_list
# Imports colored package
from colored import Fore, Style

# Gets a random word from the word list
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Game Logic
def play(word):
    # sets unguessed letters to underscores
    word_completion = "_" * len(word)
    # defines variables
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # gets pb from pb file
    f = open("pb.txt", "r")
    pb = f.read()
    f.close
    # displays current hangman and unguessed word
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("Your personal best is: ", pb)
    print("\n")
    while not guessed and tries > 0:
        # logic if the player guesses a singular letter
        guess = input("Please guess a letter or word: ").upper()
        # checks if the guess is 1 character and if it is a valid guess
        if len(guess) == 1 and guess.isalpha():
            # checks if guess is already guessed
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
                # checks if guess is incorrect
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                # handles if the guess is correct
            else:
                print("Good job, ", guess, " is in the word")
                guessed_letters.append(guess)
                # changes all underscores that are guessed to the guessed letter
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # checks if the whole word had been guessed
                if "_" not in word_completion:
                    guessed = True
        # handles if the player guesses a whole word
        elif len(guess) == len(word) and guess.isalpha():
            # handles if the player has previously guessed that word
            if guess in guessed_words:
                print("You already guessed the word", guess)
                # handles if the player guessed incorrectly
            elif guess != word:
                print(guess, " is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                # handles if the player guesses the word
                guessed = True
                word_completion = word
        else:
            # handles when the player enters an invalid character
            print("Not a valid guess.")
        # updates hangman
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    # handles player winning
    if guessed:
        print(f"{Fore.green}Woo Hoo! You guessed the word!{Style.reset}")
        # handles if the player beats their personal best
        # converts tries to guesses then writes it to the pb file and updates pb variable
        if (tries - 6) * -1 < int(pb):
            pb = (tries - 6) * -1
            f = open("pb.txt", "w")
            f.write(str(pb))
            f.close        
            print(f"{Fore.yellow}You got a new personal best! ", pb, f" guesses!{Style.reset}")
        else:
            print("Personal best: ", pb, " guesses.")
    # handles if the player runs out of tries
    else:
        print("You ran out of tries. The word was " + word)
        print("Your personal best is: ", pb, " guesses.")

# Hangman display states
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                f"""{Fore.red}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                {Style.reset}""",
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# asks the player to play again
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


# makes sure the application runs
if __name__ == "__main__":
    main()