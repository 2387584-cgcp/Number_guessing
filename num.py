import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10    import random
    
    def play_game():
        print("Welcome to the Number Guessing Game!")
        number_to_guess = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
    
        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-100): "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
    
                attempts += 1
    
                if guess == number_to_guess:
                    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                    break
                elif guess < number_to_guess:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
        else:
            print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
    
    def main():
        while True:
            play_game()
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break
    
    if __name__ == "__main__":
        main()

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == number_to_guess:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()