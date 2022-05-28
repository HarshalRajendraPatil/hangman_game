# importing different modules and files
import random
import hangman_words
import hangman_art

# Creating the global variables.
end_of_game = False;
lives = 6;
random_word = random.choice(hangman_words.word_list);
print(random_word);

# sign for number of letters for the word.
print(hangman_art.logo);
print("\n")
print("The number of letters in the word are as follows.")
display = [];
for leter in range(len(random_word)):
    display.append("_")
print(display);

while not end_of_game:
    user_guess = input("Please guess a letter: \t").lower();
    print("\n");

    if(user_guess in display):
        print(f"You have already entered the {user_guess} letter.")

    for i in range(len(random_word)):
        char = random_word[i];
        if user_guess == char:
            display[i] = user_guess;

    print(display)

    if user_guess not in random_word:
        print(f"You guessed the letter {user_guess} and that's not in the word\nYou lose a life.")
        lives -= 1;
        if lives == 0:
            end_of_game = True;
            print("You Lost :(")

    if "_" not in display:
        print("You Won!");
        end_of_game = True;

    print(hangman_art.stages[lives]);