# Terminal Application Project - Brodey Bright

This application is a game called hangman that runs in the python terminal.

## Links
- [Github Repository](https://github.com/bbrodo/BrodeyBrightT1A3)
- [Trello Board](https://trello.com/b/8pIuFl2w/t1a3)

## Code Style Guide

The code adheres to the PEP 8 Style Guide for Python, with a particular focus on following the Black Code Style and formatter for PEP8 compliance. The stylistic conventions observed include:

- A 79-character line limit.
- 4-space indentation.
- Blank lines to separate functions for improved readability.
- Lowercase variables with underscores (e.g., example_variable).
- Imports separated by lines and grouped logically.
- Consistent use of double quotes throughout the codebase.

## Features

The primary objective of the application is to entertain users with the classic game of Hangman, challenging them to think and improve their skills. Additionally, the application tracks the player's personal best score, encouraging them to strive for continual improvement and achieve the lowest score possible.

### Personal best 
The application includes a "pb" text file that stores the player's current personal best. This functionality is crucial for ensuring that the personal best feature operates effectively, as it prevents the loss of this data once the application is closed.

The personal best score is calculated when the player wins a game by comparing the current game score with the existing personal best. If the current game score is lower than the personal best, the application displays the player's new personal best and updates the "pb" text file with the new value.

### Hangman Display
The application features a visual representation of the current Hangman status, utilizing a Python list that contains different levels of completion. This list dynamically displays on the screen based on the number of attempts remaining, presenting the Hangman figure in ASCII art.

#### How it works

1. **Define Hangman stages**: Create a Python list containing ASCII art representations of the Hangman at different stages of completion.

2. **Track attempts**: Keep track of the number of incorrect guesses the player has made. For each incorrect guess, you progress to the next stage of the Hangman.

3. **Display Hangman**: Display the Hangman stage corresponding to the number of incorrect guesses using print.

4. **End game condition**: Determines when the game should end. This could happen when the Hangman is complete (the player loses) or when the word is guessed correctly (the player wins).

5. **Update display**: Continuously update the displayed Hangman after each incorrect guess.

This logic ensures that the Hangman figure is dynamically displayed on the screen based on the player's progress and adds visual engagement to the game.

### Guessing

In the application, players attempt to guess a randomly selected word from a list. They continue guessing until they either successfully complete the word or exhaust all their attempts. Throughout the game, any letters that remain undiscovered are represented by underscores, adding to the challenge and suspense of the game.

#### How it works

1. **Select a word**: The application chooses a word randomly from a predefined list of words. This word will be the target that the player has to guess.

2. **Display placeholders**: The application displays placeholders for each letter in the word. For example, if the word is "hello", it would display "_ _ _ _ _" 

3. **Accept guesses**: The application prompts the player to input a letter guess and ensures that the input is a valid letter and hasn't been guessed before.

4. **Check if guess is correct**: The application compares the guessed letter with each letter in the target word. If the guessed letter matches any letter in the word, it reveals those letters in the placeholders. If the guess is incorrect, it decrements the remaining attempts and progresses the Hangman display.

5. **Update display**: The application updates the display to reflect the current state of the word and the Hangman figure after each guess.

6. **Repeat until game ends**: The application continues accepting guesses from the player until either the word is fully guessed (player wins) or the Hangman is complete (player loses).

7. **End game**: Once the game ends, it displays a message indicating whether the player won or lost and reveals the unguessed word to the player.

## Installation

To run this application, you must have Python 3 installed.

##### Dependencies

The application uses the following dependencies which are automatically set up upon launch.
- colored==2.2.4

To install this app, download the **src** folder containing the source code of the project.

Run the **run.sh** bash script which will set up a virtual environment and start the application for you automatically.

## Using the App

Upon launching the application, you'll dive straight into a game of Hangman. Here, you'll encounter the Hangman display, the current word with unguessed letters represented by underscores, and your personal best score. You'll then be prompted to guess a letter or the entire word.

![Hangmanstart](/docs/hangman1.png)

If you guess a letter correctly, it will be revealed in the word, and you'll receive a congratulations. If the word remains incomplete, you'll be prompted to guess again. However, if your guess is incorrect, you'll lose an attempt, and the next stage of the Hangman will be displayed. If you input an invalid guess, such as "3", the game will prompt you to try again.

![Hangmanguess](/docs/hangman2.png)

This cycle continues until either you successfully guess the word or you exhaust all your attempts. If you correctly guess the word and surpass your personal best, you'll receive congratulations, and your new personal best will be saved. Once the game concludes, you'll be given the option to play again or exit the application.

![Hangmandie](/docs/hangman3.png)
![Hangmanwin](/docs/hangman4.png)

## Implementation Plan

I used a Trello board to manage and plan my project and tasks.

#### Screenshots

![Trello Board](/docs/trello1.png)
![Trello task1](/docs/trello2.png)
![Trello task2](/docs/trello3.png)
![Trello task3](/docs/trello4.png)
![Trello task4](/docs/trello5.png)