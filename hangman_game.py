import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer", "algorithm", "openai", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    
    while "_" in display_word(word_to_guess, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print("Incorrect guess. Attempts left:", attempts)
        else:
            print("Invalid input. Please enter a single letter.")
        
        print(display_word(word_to_guess, guessed_letters))
    
    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
